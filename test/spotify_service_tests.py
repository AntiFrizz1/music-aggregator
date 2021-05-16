import unittest
import yaml

from unittest.mock import Mock
from common.spotify import Spotify
from test.data import test_data


class SpotifyServiceTestCase(unittest.TestCase):

    def setUp(self):
        config_filepath = "../config.yaml"
        with open(config_filepath, "r") as f:
            try:
                config = yaml.safe_load(f)
                self.service = Spotify(config['spotify'])
            except yaml.YAMLError as exc:
                print(exc)

    def test_search_track_by_link(self):
        # given
        link = test_data.spotify_test_track_link
        self.service.client.track = Mock(return_value=test_data.spotify_api_search_track_by_link_result_json)

        # when
        actual = self.service.search_track_by_link(link)

        # then
        expected = ('I Hate Everything About You',          # track name
                    ['Three Days Grace'],                   # artists list
                    'Three Days Grace (Deluxe Version)',    # album name
                    'SpotifyqTrackq6rUp7v3l8yC4TKxAAR5Bmx') # entity id
        self.assertEqual(actual, expected)

    def test_search_track(self):
        # given
        test_artists = ['Three Days Grace']
        test_track = 'I Hate Everything About You'
        self.service.client.search = Mock(return_value=test_data.spotify_api_search_track_result_json)

        # when
        actual_link = self.service.search_track(test_track, test_artists)

        # then
        expected_link = "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
        self.assertEqual(actual_link, expected_link)
