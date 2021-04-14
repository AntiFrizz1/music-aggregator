from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from db.sql import sql_db
from db.mongo import mongo
import mongoengine as me
import datetime


def to_json_method(self):
    this_dict = {}
    for k, v in self.__dict__.items():
        if k[-4:] == '_rel':
            continue
        this_dict[k] = v

    exclude = self.exclude
    if exclude:
        for key in exclude:
            this_dict.pop(key)

    return this_dict


class User(sql_db.Model, UserMixin):
    __tablename__ = "user"

    user_id = sql_db.Column(sql_db.Integer, primary_key=True)
    username = sql_db.Column(sql_db.String(100), unique=True, nullable=False)
    password = sql_db.Column(sql_db.String(100), nullable=False)
    email = sql_db.Column(sql_db.String(100), unique=True, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    to_json_ = to_json_method


class Track(me.EmbeddedDocument):
    meta = {'allow_inheritance': True}
    album = me.StringField()
    artists = me.ListField(me.StringField(), required=True)
    track = me.StringField(required=True)
    url = me.StringField(required=True)


class QueryResult(me.EmbeddedDocument):
    service_name = me.StringField(required=True)
    tracks = me.EmbeddedDocumentListField(Track, required=True)


class History(mongo.Document):
    query = me.StringField(required=True)
    services = me.StringField()
    limit = me.IntField()
    user_id = me.IntField(required=True)
    result = me.EmbeddedDocumentListField(QueryResult, required=True)
    requested_at = me.DateTimeField(required=True, default=datetime.datetime.utcnow)


class PlaylistTrack(Track):
    service_name = me.StringField(required=True)


class Playlist(mongo.Document):
    user_id = me.IntField(required=True)
    name = me.StringField(required=True)
    description = me.StringField(required=True)
    tracks = me.EmbeddedDocumentListField(PlaylistTrack, required=True)
