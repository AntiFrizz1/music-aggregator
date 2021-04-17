import base64
import unittest
import uuid

import mongoengine
from flask_sqlalchemy import SQLAlchemy

from application import *

test_username = 'PeterTheGreat'
test_password = 'GreatToBe'
test_email = 'peters@burg.ru'


class MusicAggregatorApiTestCase(unittest.TestCase):

    def sign_up_test_user(self):
        response = self.app.post('signup/',
                                 json={"username": "%s" % test_username,
                                       "password": "%s" % test_password,
                                       "email": "%s" % test_email})
        assert response.status_code == 201

    def setUp(self):
        self.app = app.test_client()

        self.mongo_db_filename = str(uuid.uuid4())

        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['TESTING'] = True

        app.sql_db = SQLAlchemy()
        initialize_sql_db(app)
        mongoengine.connect(self.mongo_db_filename, alias='default')

        with app.app_context():
            sql_db.create_all()
        self.sign_up_test_user()

    def tearDown(self):
        mongoengine.disconnect(alias='default')

    def test_initialization(self):
        rv = self.app.get('/')
        assert rv.data == b'Hey, Im alive!'

    # when get playlist then code 200 is returned
    def test_get_playlist(self):
        creds = bytearray(test_username + ":" + test_password, "utf8")
        user_credentials = base64.b64encode(creds).decode()
        response = self.app.get('playlists/', headers={"Authorization": "Basic {}".format(user_credentials)})
        assert response.status_code == 200

    # when post playlist then code 201 is returned
    def test_post_playlist(self):
        creds = bytearray(test_username + ":" + test_password, "utf8")
        user_credentials = base64.b64encode(creds).decode()
        response = self.app.post('playlists/',
                                 json={
                                     "name": "Pop Music 2008",
                                     "description": "some popular music",
                                     "tracks": [
                                         {
                                             "track_id": "1",
                                             "service_name": "1"
                                         }
                                     ]
                                 },
                                 headers = {"Authorization": "Basic {}".format(user_credentials)})

        assert response.status_code == 201


if __name__ == '__main__':
    unittest.main()
