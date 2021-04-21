from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import Hyperlinks, URLFor
from marshmallow import Schema, fields, post_load, pre_load
from flask_httpauth import g

from db.models import Playlist, User

ma = Marshmallow()


class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    email = fields.String(required=True)

    @post_load
    def create_user(self, data, **kwargs):
        username = data['username']
        password = data['password']
        email = data['email']
        user = User(username=username, email=email)
        user.set_password(password)
        return user


class TrackSchema(Schema):
    album = fields.String(required=False)
    artists = fields.List(fields.String, required=True)
    track = fields.String(required=True)
    url = fields.String(required=True)


class QueryResultSchema(Schema):
    service_name = fields.String(required=True)
    tracks = fields.List(fields.Nested(TrackSchema), required=True)


class HistorySchema(Schema):
    query = fields.String(required=True)
    services = fields.String()
    limit = fields.Int()
    user_id = fields.Int(required=True, load_only=True)
    result = fields.List(fields.Nested(QueryResultSchema), required=True)
    requested_at = fields.DateTime(required=True)


class PlaylistTrackSchema(TrackSchema):
    service_name = fields.String(required=True)


class PlaylistSchema(Schema):
    user_id = fields.Int(required=True, load_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    tracks = fields.List(fields.Nested(PlaylistTrackSchema), required=True)

    @post_load
    def create_playlist(self, data, **kwargs):
        return Playlist(**data)

    @pre_load
    def add_user_id(self, data, **kwargs):
        data['user_id'] = g.user.user_id
        return data


class Link(Schema):
    self = fields.String(required=True)


class PlaylistsSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)

    _links = Hyperlinks(
        {
            "self": URLFor("get_playlist", values=dict(playlist_id="<id>")),
        }
    )


playlist_schema = PlaylistSchema()
playlists_schema = PlaylistsSchema(many=True)
user_schema = UserSchema()


def initialize_marshmallow(app):
    ma.init_app(app)
