import unittest

from unittest.mock import Mock
from common.spotify import Spotify
from test.data import test_data


class SpotifyTestClient:
    def track(self):
        pass

    def search(self):
        pass

    def artist(self):
        pass


class SpotifyServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.service = Spotify()
        self.service.client = SpotifyTestClient()

    def test_search_track_by_link(self):
        # given
        link = test_data.spotify_test_track_link
        self.service.client.track = Mock(return_value=test_data.spotify_api_search_track_by_link_result_json)

        # when
        actual = self.service.search_track_by_link(link)

        # then
        expected = ('I Hate Everything About You',  # track name
                    ['Three Days Grace'],  # artists list
                    'Three Days Grace (Deluxe Version)',  # album name
                    'SpotifyqTrackq6rUp7v3l8yC4TKxAAR5Bmx')  # entity id
        self.assertEqual(expected, actual)

    def test_search_track(self):
        # given
        test_artists = ['Three Days Grace']
        test_track = 'I Hate Everything About You'
        self.service.client.search = Mock(return_value=test_data.spotify_api_search_track_result_json)

        # when
        actual_link = self.service.search_track(test_track, test_artists)

        # then
        expected_link = "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
        self.assertEqual(expected_link, actual_link)

    def test_search_track_by_query(self):
        # given
        test_query = 'Three Days Grace - I Hate Everything About You'
        limit = 2
        self.service.client.search = Mock(return_value=test_data.spotify_api_search_track_result_json)

        # when
        result = self.service.search_track_by_query(test_query, limit)
        expected = test_data.spotify_api_search_track_by_query_extracted_result_with_limit_2

        # then
        self.assertTrue(len(result['tracks']) <= limit)
        self.assertEqual(expected, result)

    def test_search_artist_by_link(self):
        # given
        link = "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
        self.service.client.artist = Mock(return_value=test_data.spotify_test_artist_tdg)

        # when
        actual = self.service.search_artist_by_link(link)

        # then
        expected = ('Three Days Grace', 'SpotifyqArtistq2xiIXseIJcq3nG7C8fHeBj')
        self.assertEqual(expected, actual)

    def test_search_album_by_link(self):
        # given
        link = "https://open.spotify.com/album/13topfW33NjnACjnRiZBX7"
        self.service.client.album = Mock(return_value=test_data.spotify_test_album_tdg)

        # when
        actual = self.service.search_album_by_link(link)

        # then
        expected = ('Three Days Grace', 'SpotifyqAlbumq13topfW33NjnACjnRiZBX7')
        self.assertEqual(expected, actual)

    def test_search_artist(self):
        # given
        name = "Linkin Park"
        self.service.client.search = Mock(return_value=test_data.spotify_test_artist_lp)

        # when
        actual = self.service.search_artist(name)

        # then
        expected = "https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz"
        self.assertEqual(expected, actual)

    def test_search_album(self):
        # given
        name = "Meteora"
        self.service.client.search = Mock(return_value=test_data.spotify_test_album_meteora)

        # when
        actual = self.service.search_album(name)

        # then
        expected = "https://open.spotify.com/album/4Gfnly5CzMJQqkUFfoHaP3"
        self.assertEqual(expected, actual)

    def test_detect_entity_by_link(self):
        album_link = "https://open.spotify.com/album/13topfW33NjnACjnRiZBX7"
        track_link = "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
        artist_link = "https://music.apple.com/ru/artist/three-days-grace/1973668?uo=4"

        self.assertEqual(self.service.Entity.Album, self.service.detect_entity_by_link(album_link))
        self.assertEqual(self.service.Entity.Track, self.service.detect_entity_by_link(track_link))
        self.assertEqual(self.service.Entity.Artist, self.service.detect_entity_by_link(artist_link))

    def test_entity_type_to_string(self):
        self.assertEqual("album", self.service._entity_type_to_string(self.service.Entity.Album))
        self.assertEqual("track", self.service._entity_type_to_string(self.service.Entity.Track))
        self.assertEqual("artist", self.service._entity_type_to_string(self.service.Entity.Artist))

    def test_extract_track_data(self):
        # given
        track_json = test_data.spotify_test_track_json

        # when
        actual = self.service._extract_track_data(track_json)

        # then
        expected = {'track': 'I Hate Everything About You - Live Acoustic - Rolling Stone Original (EP)',
                    'album': 'Rolling Stone Original (EP)',
                    'artists': ['Three Days Grace'],
                    'url': 'https://open.spotify.com/track/7e2073Iang0hKXlFoffwpF'}
        self.assertEqual(expected, actual)

    def test_extract_album_data(self):
        # given
        album_json = test_data.spotify_test_album_json

        # when
        actual = self.service._extract_album_data(album_json)

        # then
        expected = {'album': 'Moral Panic',
                    'artists': ['Nothing But Thieves'],
                    'url': 'https://open.spotify.com/album/5LNmaMITXXVrEm4fnyUbrd'}
        self.assertEqual(expected, actual)

    def test_extract_artist_data(self):
        # given
        artist_json = test_data.spotify_test_artist_json

        # when
        actual = self.service._extract_artist_data(artist_json)

        # then
        expected = {'artist': 'PVRIS',
                    'url': 'https://open.spotify.com/artist/6oFs3qk4VepIVFdoD4jmsy'}
        self.assertEqual(expected, actual)

    def test_extract_search_data(self):
        track_json = test_data.spotify_test_track_json
        album_json = test_data.spotify_test_album_json
        artist_json = test_data.spotify_test_artist_json

        expected_track = {'track': 'I Hate Everything About You - Live Acoustic - Rolling Stone Original (EP)',
                    'album': 'Rolling Stone Original (EP)',
                    'artists': ['Three Days Grace'],
                    'url': 'https://open.spotify.com/track/7e2073Iang0hKXlFoffwpF'}

        expected_album = {'album': 'Moral Panic',
                    'artists': ['Nothing But Thieves'],
                    'url': 'https://open.spotify.com/album/5LNmaMITXXVrEm4fnyUbrd'}

        expected_artist = {'artist': 'PVRIS',
                    'url': 'https://open.spotify.com/artist/6oFs3qk4VepIVFdoD4jmsy'}

        self.assertEqual(expected_album, self.service._extract_search_data(album_json, self.service.Entity.Album))
        self.assertEqual(expected_track, self.service._extract_search_data(track_json, self.service.Entity.Track))
        self.assertEqual(expected_artist, self.service._extract_search_data(artist_json, self.service.Entity.Artist))

    def test_search_by_query(self):
        search_artist_query = "PVRIS"
        total_artists = len(test_data.spotify_search_artists_by_query_json['artists']['items'])
        print(total_artists)
        self.service.client.search = Mock(return_value=test_data.spotify_search_artists_by_query_json)
        for limit in range(1, total_artists):
            result = self.service.search_by_query(search_artist_query, self.service.Entity.Artist, limit)
            total_entries = len(result['artists'])
            print(limit, total_entries)
            self.assertTrue(total_entries == min(total_artists, limit))
