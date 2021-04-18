import base64
import unittest
import uuid
from wsgiref.headers import Headers
from urllib.parse import urlparse

import mongoengine
from flask_sqlalchemy import SQLAlchemy

from application import *

test_username = 'PeterTheGreat'
test_password = 'GreatToBe'
test_email = 'peters@burg.ru'

playlist_data = {
    "name": "Pop Music 2008",
    "description": "some popular music",
    "tracks": [
        {
            "service_name": "service1",
            "album": "Album1",
            "artists": [
                "Artist1",
                "Artist2"
            ],
            "track": "Best track 1",
            "url": "https://open.spotify.com/track/track_id"
        },
        {
            "service_name": "service2",
            "album": "Album2",
            "artists": [
                "Artist1",
                "Artist2",
                "Artist3"
            ],
            "track": "Best track 2",
            "url": "https://music.yandex.ru/album/abum_id/track/track_id"
        }
    ]
}


def extract_path(url):
    return urlparse(url).path


class MusicAggregatorApiTestCase(unittest.TestCase):

    def sign_up_test_user(self):
        user_data = {"username": "%s" % test_username,
                     "password": "%s" % test_password,
                     "email": "%s" % test_email}
        response = self.app.post('signup', json=user_data)
        assert response.status_code == 200
        assert response.json == user_schema.dump(user_data)

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

        creds = bytearray(test_username + ":" + test_password, "utf8")
        self.user_credentials = base64.b64encode(creds).decode()

    def tearDown(self):
        mongoengine.disconnect(alias='default')

    def test_initialization(self):
        rv = self.app.get('/')
        assert rv.data == b'Hey, Im alive!'

    # when get playlist then code 200 is returned
    def test_get_empty_playlists(self):
        response = self.app.get('playlists/', headers={"Authorization": "Basic {}".format(self.user_credentials)})
        assert response.status_code == 200
        assert response.json.empty()

    def _provision_playlist(self):
        response = self.app.post('playlists/',
                                 json=playlist_data,
                                 headers={"Authorization": "Basic {}".format(self.user_credentials)})
        headers: Headers = response.headers
        location = headers.get('Location')
        assert location
        return response, extract_path(location)

    # when post playlist then code 201 is returned
    def test_post_playlist(self):
        response, _ = self._provision_playlist()
        assert response.status_code == 201
        assert response.json == playlist_data

    # when put playlist then code 200 is returned
    def test_put_playlist(self):
        _, location = self._provision_playlist()
        edited_playlist = playlist_data.copy()
        edited_playlist['name'] = "New playlist name"
        edited_playlist['tracks'].pop(0)
        response = self.app.put(location,
                                 json=edited_playlist,
                                 headers={"Authorization": "Basic {}".format(self.user_credentials)})
        assert response.status_code == 200
        assert response.json == edited_playlist

    # when get playlists then code 200 is returned
    def test_get_playlist(self):
        _, location = self._provision_playlist()
        response = self.app.get(location, headers={"Authorization": "Basic {}".format(self.user_credentials)})
        assert response.status_code == 200
        assert response.json == playlist_data

    # when delete playlist then code 204 is returned
    def test_delete_playlist(self):
        _, location = self._provision_playlist()
        response = self.app.delete(location, headers={"Authorization": "Basic {}".format(self.user_credentials)})
        assert response.status_code == 204

        response = self.app.get(location, headers={"Authorization": "Basic {}".format(self.user_credentials)})
        assert response.status_code == 404

    # when get playlists then code 200 is returned
    def test_get_playlists(self):
        playlists_locations = [ self._provision_playlist()[1] for _ in range(2)]
        playlists_data = [
            {
                "_links": { 'self': location },
                'name': playlist_data['name'],
                "description": playlist_data['description']
            } for location in playlists_locations
        ]
        response = self.app.get('playlists/', headers={"Authorization": "Basic {}".format(self.user_credentials)})
        assert response.status_code == 200
        assert response.json == playlists_data


if __name__ == '__main__':
    unittest.main()
