import unittest
from unittest.mock import Mock
from common.music_service import MusicService


class MusicServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.service = MusicService()

    def test_get_entity_id(self):
        self.verify_entity_id("album_id", self.service.Entity.Album)
        self.verify_entity_id("track_id", self.service.Entity.Track)
        self.verify_entity_id("artist_id", self.service.Entity.Artist)

    def verify_entity_id(self, entity_id, entity_type):
        actual_entity_id = self.service._get_entity_id(entity_id, entity_type)
        expected_entity_id = MusicService.name + "q" + entity_type.name + "q" + entity_id
        self.assertEqual(actual_entity_id, expected_entity_id)

    def test_entity_to_plural_str(self):
        self.assertEqual(self.service._entity_to_plural_str(self.service.Entity.Album), "albums")
        self.assertEqual(self.service._entity_to_plural_str(self.service.Entity.Track), "tracks")
        self.assertEqual(self.service._entity_to_plural_str(self.service.Entity.Artist), "artists")

    def test_search_by_link(self):
        album_link = "https://open.spotify.com/album/13topfW33NjnACjnRiZBX7"
        track_link = "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
        artist_link = "https://music.apple.com/ru/artist/three-days-grace/1973668?uo=4"

        self.service.detect_entity_by_link = Mock(return_value=self.service.Entity.Album)
        self.service.search_album_by_link = Mock(return_value=["album", "album_id"])
        self.service.search_by_link(album_link)
        self.service.search_album_by_link.assert_called_with(album_link)

        self.service.detect_entity_by_link = Mock(return_value=self.service.Entity.Track)
        self.service.search_track_by_link = Mock(return_value=["track", "track_id"])
        self.service.search_by_link(track_link)
        self.service.search_track_by_link.assert_called_with(track_link)

        self.service.detect_entity_by_link = Mock(return_value=self.service.Entity.Artist)
        self.service.search_artist_by_link = Mock(return_value=["artist", "artist_id"])
        self.service.search_by_link(artist_link)
        self.service.search_artist_by_link.assert_called_with(artist_link)

    def test_search_by_entity(self):
        entity_name = "some_entity_name"
        result_link = "https://some.link.for.entity"

        self.service.search_album = Mock(return_value=result_link)
        self.service.search_by_entity(self.service.Entity.Album, entity_name)
        self.service.search_album.assert_called_with(*entity_name)

        self.service.search_artist = Mock(return_value=result_link)
        self.service.search_by_entity(self.service.Entity.Artist, entity_name)
        self.service.search_artist.assert_called_with(*entity_name)

        self.service.search_track = Mock(return_value=result_link)
        self.service.search_by_entity(self.service.Entity.Track, entity_name)
        self.service.search_track.assert_called_with(*entity_name)
