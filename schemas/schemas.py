from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import Hyperlinks, URLFor
from marshmallow import Schema, fields, post_load, post_dump

from db.models import Playlist

ma = Marshmallow()


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


class Link(Schema):
    self = fields.String(required=True)


class PlaylistsSchema(Schema):
    name = fields.String(required=True)
    description = fields.String(required=True)

    _links = Hyperlinks(
        {
            "self": URLFor("process_playlist", values=dict(playlist_id="<id>")),
        }
    )


playlist_schema = PlaylistSchema()
playlists_schema = PlaylistsSchema(many=True)


def initialize_marshmallow(app):
    ma.init_app(app)
