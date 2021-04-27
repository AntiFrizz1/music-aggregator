import yaml
import json
import functools
import os

from flask import Flask, url_for, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth, g
from mongoengine import ValidationError, DoesNotExist
from webargs import fields, validate, flaskparser
from webargs.flaskparser import use_args

from common.spotify import Spotify
from common.ya_music import YandexMusic
from db.models import User, Playlist, History
from db.sql import sql_db, initialize_sql_db
from db.mongo import initialize_mongo_db
from schemas.schemas import initialize_marshmallow, playlist_schema, playlists_schema, user_schema

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MONGODB_SETTINGS'] = {
    "db": "music_aggregator",
    'host': 'mongodb://root:rootpassword@localhost:27017/music_aggregator'
}

services = {}


@flaskparser.parser.error_handler
def arg_parser_error_handle(error, req, schema, *, error_status_code, error_headers):
    status_code = error_status_code or 400
    abort(status_code)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": 'Bad request.'}), 400


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": error.description}), 404


@app.errorhandler(501)
def not_implemented(error):
    return jsonify({"error": 'Not implemented.'}), 501


@app.errorhandler(500)
def server_internal_error(error):
    return jsonify({"error": 'Server internal error.'}), 500


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/signup', methods=['POST'])
@use_args(user_schema, location='json')
def signup(received_user):
    user = sql_db.session.query(User).filter(User.username == received_user.username).first()
    if user:
        return jsonify({"error": 'User "%s" already exist.' % received_user.username}), 400

    user = received_user
    sql_db.session.add(user)
    sql_db.session.commit()

    return jsonify(user_schema.dump(user)), 200


@app.route('/playlists/', methods=['POST'])
@auth.login_required
@use_args(playlist_schema, location='json')
def add_playlist(playlist):
    playlist.save()
    return jsonify(request.json), 201, {'Location': url_for('get_playlist', playlist_id=str(playlist.id))}


@app.route('/playlists/', methods=['GET'])
@auth.login_required
def get_playlists():
    playlists_json = playlists_schema.dump(Playlist.objects(user_id=g.user.user_id), many=True)
    return jsonify(playlists_json), 200


def retrieve_playlist_from_db(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        playlist = None
        playlist_id = kwargs['playlist_id']
        try:
            playlist = Playlist.objects(id=playlist_id).get()
        except DoesNotExist:
            pass
        except ValidationError:
            abort(500)

        if (not playlist) or (playlist.user_id != g.user.user_id):
            abort(404, 'Playlist "%s" not found.' % playlist_id)
        kwargs.update({"db_playlist": playlist})
        return func(*args, **kwargs)

    wrapper.__wrapped__ = func
    return wrapper


@app.route("/playlists/<string:playlist_id>", methods=['PUT'])
@auth.login_required
@use_args(playlist_schema, location='json')
@retrieve_playlist_from_db
def update_playlist(received_playlist, playlist_id, db_playlist):
    received_playlist.id = db_playlist.id
    received_playlist.save()
    return jsonify(playlist_schema.dump(received_playlist)), 200, {'Location': url_for('get_playlist', playlist_id=playlist_id)}


@app.route("/playlists/<string:playlist_id>", methods=['GET'])
@auth.login_required
@retrieve_playlist_from_db
def get_playlist(playlist_id, db_playlist):
    return playlist_schema.dump(db_playlist), 200


@app.route("/playlists/<string:playlist_id>", methods=['DELETE'])
@auth.login_required
@retrieve_playlist_from_db
def delete_playlist(playlist_id, db_playlist):
    db_playlist.delete()
    return jsonify(), 204


search_args = {
    "q": fields.Str(required=True, validate=validate.Length(min=3)),
    "limit": fields.Int(validate=lambda val: val > 0),
    "services": fields.DelimitedList(fields.Str(), validate=validate.Length(min=1))
}


@app.route("/search", methods=['GET'])
@auth.login_required
@use_args(search_args, location="query")
def search(args):
    query = args['q']
    service_names = args.get('services')
    limit = args.get('limit')

    search_in_services = {}
    if not service_names:
        search_in_services = services
    else:
        for service_name in service_names:
            if services.get(service_name):
                search_in_services[service_name] = services[service_name]
            else:
                abort(400)
    try:
        if limit:
            limit = int(limit)
    except ValueError:
        abort(400)

    result = []
    for service in search_in_services.values():
        result.append(service.search_track_by_query(query, limit))
    history_json = {
        'query': query,
        'result': result,
        'user_id': g.user.user_id
    }
    if service_names:
        history_json['services'] = ",".join(service_names)
    if limit:
        history_json['limit'] = limit
    history = History.from_json(json.dumps(history_json))
    history.save()
    return jsonify(result), 200


@app.route('/')
def check_if_alive():
    return 'Hey, Im alive!'


def init_app():
    app.app_context().push()
    initialize_sql_db(app)
    initialize_mongo_db(app)
    initialize_marshmallow(app)

    config_filepath = "config.yaml"
    services[YandexMusic.name] = YandexMusic()
    with open(config_filepath, "r") as f:
        try:
            config = yaml.safe_load(f)
            services[Spotify.name] = Spotify(config['spotify'])
        except yaml.YAMLError as exc:
            print(exc)

    sql_db.create_all()


if __name__ == '__main__':
    init_app()
    # app.run(debug=True)
