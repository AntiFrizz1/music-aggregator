import yaml
import json

from flask import Flask, url_for, jsonify, request
from flask_httpauth import HTTPBasicAuth, g
from mongoengine import ValidationError, DoesNotExist

from common.spotify import Spotify
from common.ya_music import YandexMusic
from db.models import User, Playlist, History
from db.sql import sql_db, initialize_sql_db
from db.mongo import initialize_mongo_db
from schemas.schemas import initialize_marshmallow, playlist_schema, playlists_schema

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['MONGODB_SETTINGS'] = {"db": "myapp"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

services = []


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/signup/', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')

    if not (username and email and password):
        return jsonify({"error": 'Bad request.'}), 400

    user = sql_db.session.query(User).filter(User.username == username).first()
    if user:
        return jsonify({"error": 'User "%s" already exist.' % username}), 400

    user = User(username=username, email=email)
    user.set_password(password)
    sql_db.session.add(user)
    sql_db.session.commit()

    return jsonify({'username': username, 'email': email}), 201


def add_user_id(object_json):
    output_json = object_json.copy()
    output_json['user_id'] = g.user.user_id
    return output_json


@app.route('/playlists/', methods=['POST', 'GET'])
@auth.login_required
def process_playlists():
    if request.method == 'POST':
        request_json = add_user_id(request.json)
        playlist = Playlist.from_json(json.dumps(request_json))
        try:
            playlist.validate()
            playlist.save()
            return jsonify(request.json), 201, {'Location': url_for('process_playlist', playlist_id=str(playlist.id))}
        except ValidationError:
            return jsonify({"error": "Bad request."}), 400
    else:
        playlists_json = playlists_schema.dump(Playlist.objects(user_id=g.user.user_id), many=True)
        return jsonify(playlists_json), 200


@app.route("/playlists/<string:playlist_id>", methods=['PUT', 'GET', 'PATCH', 'DELETE'])
@auth.login_required
def process_playlist(playlist_id):
    try:
        playlist = Playlist.objects(id=playlist_id).get()
    except DoesNotExist:
        playlist = None
    except ValidationError:
        return jsonify({'error': 'Internal server error.'}), 500

    if (not playlist) or (playlist.user_id != g.user.user_id):
        return jsonify({'error': 'Playlist "%s" not found.' % playlist_id}), 404

    if request.method == 'PUT':
        playlist_json = add_user_id(request.json)
        if len(playlist_schema.validate(playlist_json)) != 0:
            return jsonify({'error': 'Bad request.'}), 400
        playlist = playlist_schema.load(playlist_json)
        playlist.save()
        return jsonify(request.json), 200, {'Location': url_for('process_playlist', playlist_id=str(playlist.id))}

    if request.method == 'GET':
        return playlist_schema.dump(playlist), 201

    if request.method == 'DELETE':
        playlist.delete()
        return jsonify(), 204

    return jsonify(), 501


@app.route("/search", methods=['GET'])
@auth.login_required
def search():
    query = request.args.get('q')
    service_names = request.args.get('services')
    limit = request.args.get('limit')
    search_in_services = []
    if not query:
        return jsonify({'error': "Expected path variable q."}), 400
    if not service_names:
        search_in_services = services
    else:
        service_names_list = service_names.split(' ')
        for service_name in service_names_list:
            find_service = False
            for service in services:
                if service_name == service.name:
                    search_in_services.append(service)
                    find_service = True
                    break
            if not find_service:
                return jsonify({'error': "Unknown service name %s" % service_name}), 400
    try:
        if limit:
            limit = int(limit)
    except:
        return jsonify({'error': "Incorrect limit value %s" % limit}), 400

    result = []
    for service in search_in_services:
        result.append(service.search_track_by_query(query, limit))
    history_json = {
        'query': query,
        'result': result,
        'user_id': g.user.user_id
    }
    if service_names:
        history_json['services'] = service_names
    if limit:
        history_json['limit'] = limit
    history = History.from_json(json.dumps(history_json))
    history.save()
    return jsonify(result), 200


@app.route('/')
def check_if_alive():
    return 'Hey, Im alive!'


if __name__ == '__main__':
    app.app_context().push()
    initialize_sql_db(app)
    initialize_mongo_db(app)
    initialize_marshmallow(app)

    config_filepath = "config.yaml"
    services.append(YandexMusic())
    # services.append(AppleMusic())
    with open(config_filepath, "r") as f:
        try:
            config = yaml.safe_load(f)
            services.append(Spotify(config['spotify']))
        except yaml.YAMLError as exc:
            print(exc)

    sql_db.create_all()
    app.run(debug=True)
