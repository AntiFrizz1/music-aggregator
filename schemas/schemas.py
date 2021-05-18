from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import Hyperlinks, URLFor
from marshmallow import Schema, fields, post_load, pre_load
from marshmallow import validate
from flask_httpauth import g

from db.models import Playlist, User

ma = Marshmallow()


class UserRequestSchema(Schema):
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


class UserResponseSchema(Schema):
    username = fields.String(required=True)
    email = fields.String(required=True)


class TrackSchema(Schema):
    album = fields.String(required=False)
    artists = fields.List(fields.String, required=True)
    track = fields.String(required=True)
    url = fields.String(required=True)


class AlbumSchema(Schema):
    album = fields.String(required=False)
    artists = fields.List(fields.String, required=True)
    url = fields.String(required=True)


class ArtistSchema(Schema):
    artist = fields.String(required=True)
    url = fields.String(required=True)


class SearchResultSchema(Schema):
    service_name = fields.String(required=True)
    tracks = fields.List(fields.Nested(TrackSchema))
    albums = fields.List(fields.Nested(AlbumSchema))
    artists = fields.List(fields.Nested(ArtistSchema))


class HistorySchema(Schema):
    query = fields.String(required=True)
    services = fields.String()
    limit = fields.Int()
    user_id = fields.Int(required=True, load_only=True)
    result = fields.List(fields.Nested(SearchResultSchema), required=True)
    requested_at = fields.DateTime(required=True)


class PlaylistTrackSchema(TrackSchema):
    service_name = fields.String(required=True)


class PlaylistSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)
    tracks = fields.List(fields.Nested(PlaylistTrackSchema), required=True)

    @post_load
    def create_playlist(self, data, **kwargs):
        data['user_id'] = g.user.user_id
        return Playlist(**data)


class PlaylistsSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)

    _links = Hyperlinks(
        {
            "self": URLFor("playlistapi", values=dict(playlist_id="<id>"), _external=True, required=True),
        },
        required=True
    )


class AsyncSearchResultId(Schema):
    result_id = fields.String(required=True)


class AsyncSearchResult(Schema):
    result = fields.Nested(SearchResultSchema(many=True))
    status = fields.String(required=True,
                           validate=validate.OneOf(
                               ['PENDING', 'STARTED', 'RETRY', 'FAILURE', 'SUCCESS']
                           ))


playlist_schema = PlaylistSchema()
playlists_schema = PlaylistsSchema(many=True)
user_request_schema = UserRequestSchema()
user_response_schema = UserResponseSchema()
search_results_schema = SearchResultSchema(many=True)


def initialize_marshmallow(app):
    ma.init_app(app)
