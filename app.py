import functools
import os
import yaml

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, url_for, request, abort, make_response
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_httpauth import HTTPBasicAuth, g
from flask_restful import Resource, Api
from mongoengine import ValidationError, DoesNotExist
from webargs import fields, validate, flaskparser

from common.apple_music import AppleMusic
from common.music_service import MusicService
from common.spotify import Spotify, validate_spotify_config
from common.ya_music import YandexMusic
from db.models import User, Playlist
from db.sql import sql_db, initialize_sql_db
from db.mongo import initialize_mongo_db
from schemas.schemas import initialize_marshmallow, playlist_schema, playlists_schema, user_request_schema, \
    user_response_schema, search_results_schema, AsyncSearchResultId, AsyncSearchResult
from make_celery import make_celery

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///tmp.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MONGODB_SETTINGS'] = {
    "host": 'mongodb://' + os.getenv('MONGODB_USERNAME', 'user') + ':' + os.getenv('MONGODB_PASSWORD', 'password') + '@'
            + os.getenv('MONGODB_HOSTNAME', 'localhost') + ':27017/' + os.getenv('MONGODB_DATABASE', 'my_db')
}
services = {}
api = Api(app)
app.config['CELERY_BROKER_URL'] = os.getenv("REDIS_URL", 'redis://localhost:6379')
app.config['CELERY_RESULT_BACKEND'] = os.getenv("REDIS_URL", 'redis://localhost:6379')
app.config['CELERY_RESULT_EXPIRES'] = 300
app.config['CELERY_TRACK_STARTED'] = True
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Music Aggregator',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})

docs = FlaskApiSpec(app)
celery = make_celery(app)


@flaskparser.parser.error_handler
def arg_parser_error_handle(error, req, schema, *, error_status_code, error_headers):
    status_code = error_status_code or 400
    abort(status_code)


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


class SignupApi(MethodResource, Resource):
    @doc(description='Client registration method', tags=['Authentication'])
    @use_kwargs(user_request_schema, location=('json'))
    @marshal_with(user_response_schema, code=201)  # marshalling
    def post(self, received_user):
        user = sql_db.session.query(User).filter(User.username == received_user.username).first()
        if user:
            abort(400, 'User "%s" already exist.' % received_user.username)

        user = received_user
        sql_db.session.add(user)
        sql_db.session.commit()

        return user_response_schema.dump(user), 201


class PlaylistsApi(MethodResource):
    @auth.login_required
    @doc(description='Add new playlist', tags=['Playlists'])
    @use_kwargs(playlist_schema, location='json')
    @marshal_with(playlist_schema, 201)
    def post(self, playlist):
        playlist.save()
        return request.json, 201, {'Location': url_for('playlistapi', playlist_id=str(playlist.id))}

    @doc(description='Retrieve all user playlists', tags=['Playlists'])
    @auth.login_required
    @marshal_with(playlists_schema, 200)
    def get(self):
        playlists = Playlist.objects(user_id=g.user.user_id)
        return playlists, 200


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


class PlaylistApi(MethodResource):
    @doc(description="Retrieve user's playlist by playlist_id", tags=['Playlists'])
    @auth.login_required
    @marshal_with(playlist_schema, 200)
    @retrieve_playlist_from_db
    def get(self, playlist_id, db_playlist):
        return playlist_schema.dump(db_playlist), 200

    @doc(description="Delete user's playlist by playlist_id", tags=['Playlists'])
    @auth.login_required
    @marshal_with(None, 204)
    @retrieve_playlist_from_db
    def delete(self, playlist_id, db_playlist):
        db_playlist.delete()
        return make_response('', 204)

    @doc(description="Update user's playlist by playlist_id", tags=['Playlists'])
    @auth.login_required
    @use_kwargs(playlist_schema, location='json')
    @retrieve_playlist_from_db
    def put(self, received_playlist, playlist_id, db_playlist):
        received_playlist.id = db_playlist.id
        received_playlist.save()
        return playlist_schema.dump(received_playlist), 200


search_args = {
    "q": fields.Str(required=True, validate=validate.Length(min=3)),
    "limit": fields.Int(validate=lambda val: val > 0, missing=5),
    "services": fields.List(
        fields.Str(validate=validate.OneOf(['AppleMusic', 'Spotify', 'YandexMusic'])),
        validate=validate.Length(min=1)
    ),
    "entity": fields.Str(required=True, validate=validate.OneOf(['track', 'album', 'artist']))
}


def search_func(query, service_names, limit, entity_name, app_services):
    search_in_services = {}
    if not service_names:
        search_in_services = app_services
    else:
        for service_name in service_names:
            search_in_services[service_name] = app_services[service_name]

    if entity_name == 'track':
        entity = MusicService.Entity.Track
    elif entity_name == 'artist':
        entity = MusicService.Entity.Artist
    else:
        entity = MusicService.Entity.Album

    result = []
    for service in search_in_services.values():
        result.append(service.search_by_query(query, entity, limit))
    return result


class SearchApi(MethodResource):
    @doc(description="Search track, album and artist by given query", tags=['Search'])
    @auth.login_required
    @use_kwargs(search_args, location="query")
    @marshal_with(search_results_schema, 200)
    def get(self, **kwargs):
        query = kwargs['q']
        service_names = kwargs.get('services')
        limit = kwargs['limit']
        entity_name = kwargs['entity']

        result = search_func(query, service_names, limit, entity_name, services)
        # history_json = {
        #     'query': query,
        #     'result': result
        #     'user_id': g.user.user_id
        # }
        # if service_names:
        #     history_json['services'] = ",".join(service_names)
        # if limit:
        #     history_json['limit'] = limit
        # history = History.from_json(json.dumps(history_json))
        # history.save()
        return result, 200


@celery.task
def background_search(query, service_names, limit, entity_name, user_id):
    global services
    result = search_func(query, service_names, limit, entity_name, services)
    return {'result': result, '_user_id': user_id}


class AsyncSearchApi(MethodResource):
    @doc(description="Async search track, album and artist by given query", tags=['Search'])
    @auth.login_required
    @use_kwargs(search_args, location="query")
    @marshal_with(AsyncSearchResultId, 200)
    def get(self, **kwargs):
        query = kwargs['q']
        service_names = kwargs.get('services')
        limit = kwargs['limit']
        entity_name = kwargs['entity']
        async_result = background_search.apply_async(args=[query, service_names, limit, entity_name, g.user.user_id])
        return {'result_id': async_result.id}, 200


class AsyncSearchResultApi(MethodResource):
    @doc(description="Retrieve result of async search", tags=['Search'])
    @auth.login_required
    @marshal_with(AsyncSearchResult, 200)
    def get(self, result_id):
        async_result = celery.AsyncResult(result_id)
        status: str = async_result.status
        if async_result.ready() and status == 'SUCCESS':
            result = async_result.get()
            if result['_user_id'] == g.user.user_id:
                return {'status': status, 'result': result['result']}, 200
            else:
                abort(401)
        return {'status': status}


api.add_resource(SignupApi, '/signup')
api.add_resource(PlaylistsApi, '/playlists/')
api.add_resource(PlaylistApi, '/playlists/<playlist_id>')
api.add_resource(SearchApi, '/search')
api.add_resource(AsyncSearchApi, '/async-search')
api.add_resource(AsyncSearchResultApi, '/async-search-result/<result_id>')

docs.register(SignupApi)
docs.register(PlaylistsApi)
docs.register(PlaylistApi)
docs.register(SearchApi)
docs.register(AsyncSearchApi)
docs.register(AsyncSearchResultApi)


def init_services():
    config_filepath = "config.yaml"
    services[YandexMusic.name] = YandexMusic()
    services[AppleMusic.name] = AppleMusic()
    with open(config_filepath, "r") as f:
        try:
            config = yaml.safe_load(f)
            spotify_config = config['spotify']
            result, message = validate_spotify_config(spotify_config)
            if not result:
                print(message)
                return
            services[Spotify.name] = Spotify(spotify_config['client_id'], spotify_config['client_secret'])
        except yaml.YAMLError as exc:
            print(exc)


init_services()


def init_app():
    app.app_context().push()
    initialize_sql_db(app)
    initialize_mongo_db(app)
    initialize_marshmallow(app)

    with app.app_context():
        sql_db.create_all()


def run():
    init_app()
    return app

if __name__ == '__main__':
    init_app()
    app.run(debug=True)
