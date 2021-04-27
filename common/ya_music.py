import re
from yandex_music import Client
from common.music_service import MusicService


class YandexMusic(MusicService):
    name = "YandexMusic"

    def __init__(self):
        self.client = Client()
        self.url_regex = re.compile(
            r'((http|https)://)?(www\.)?music\.yandex\.(ru|com)\/album\/([0-9]+)\/track\/([0-9]+)'
        )
        self.url_without_album_regex = re.compile(
            r'((http|https)://)?(www\.)?music\.yandex\.(ru|com)\/track\/([0-9]+)'
        )
        self.url_artist_regex = re.compile(
            r'((http|https)://)?(www\.)?music\.yandex\.(ru|com)\/artist\/([0-9]+)'
        )
        self.url_album_regex = re.compile(
            r'((http|https)://)?(www\.)?music\.yandex\.(ru|com)\/album\/([0-9]+)'
        )
    # link example: https://music.yandex.ru/album/43233/track/418016
    # regex: ((http|https)://)?(www\.)?music\.yandex\.(ru|com)\/album\/([0-9]+)\/track\/([0-9]+)
    # link example: https://music.yandex.ru/track/418016
    # regex: ((http|https)://)?(www\.)?music\.yandex\.(ru|com)\/track\/([0-9]+)

    @staticmethod
    def get_track_id_from_match(match):
        return match[6] + ":" + match[5]

    @staticmethod
    def get_entity_id_from_match(match):
        return match[5]

    def search_track_by_link(self, link):
        match = self.url_regex.match(link)
        if not match is None:
            track_id = self.get_track_id_from_match(match)
        else:
            match = self.url_without_album_regex.match(link)
            if match is None:
                return None
            track_id = self.get_entity_id_from_match(match)
        tracks = self.client.tracks([track_id])
        if len(tracks) == 0:
            return None
        else:
            track = tracks[0].title
            artists = [artist.name for artist in tracks[0].artists]
            album = tracks[0].albums[0].title if len(tracks[0].albums) != 0 else None
            return track, artists, album, self._get_entity_id(track_id, self.Entity.Track)

    def search_track(self, track, artists, album=None):
        query = ', '.join(artists) + " - " + track
        result = self.client.search(text=query, type_='track')
        if not result.tracks or result.tracks.total == 0:
            return None
        id = result.tracks.results[0].track_id
        if id.find(":") != -1:
            track_id, album_id = id.split(':')
            return "https://music.yandex.ru/album/%s/track/%s" % (album_id, track_id)
        else:
            return "https://music.yandex.ru/track/%s" % id

    def search_track_by_query(self, query, limit=None):
        if not limit:
            limit = self.default_limit

        result = self.client.search(text=query, type_='track')
        if not result.tracks or result.tracks.total == 0:
            return []
        tracks = result.tracks.results[:limit]

        track_list = []
        for track in tracks:
            track_json = {
                'track': track.title,
                'artists': [artist.name for artist in track.artists],
            }
            if len(track.track_id.split(':')) == 2:
                track_id, album_id = track.track_id.split(':')
                track_json['url'] = "https://music.yandex.ru/album/%s/track/%s" % (album_id, track_id)
            else:
                track_json['url'] = "https://music.yandex.ru/track/%s" % track.track_id
            if track.albums and len(track.albums) > 0:
                track_json['album'] = track.albums[0].title
            track_list.append(track_json)
        response = {
            'service_name': self.name,
            'tracks': track_list
        }
        return response

    # https://music.yandex.ru/artist/41126
    def search_artist_by_link(self, link):
        match = self.url_artist_regex.match(link)
        if match:
            artist_id = self.get_entity_id_from_match(match)
        else:
            return None

        artists = self.client.artists(artist_id)
        if len(artists) == 0:
            return None
        else:
            return artists[0].name, self._get_entity_id(artist_id, self.Entity.Artist)

    def search_artist(self, name):
        result = self.client.search(text=name, type_='artist')
        if not result.artists or result.artists.total == 0:
            return None
        artist_id = result.artists.results[0].id
        return "https://music.yandex.ru/artist/%s" % artist_id

    # https://music.yandex.ru/album/14619914
    def search_album_by_link(self, link):
        match = self.url_album_regex.match(link)
        if match:
            album_id = self.get_entity_id_from_match(match)
        else:
            return None

        albums = self.client.albums(album_id)
        if len(albums) == 0:
            return None
        else:
            return albums[0].title, self._get_entity_id(album_id, self.Entity.Album)

    def search_album(self, name):
        result = self.client.search(text=name, type_='album')
        if not result.albums or result.albums.total == 0:
            return None
        album_id = result.albums.results[0].id
        return "https://music.yandex.ru/album/%s" % album_id

    def detect_entity_by_link(self, link):
        if link.find("track") != -1:
            return self.Entity.Track
        elif link.find('album') != -1:
            return self.Entity.Album
        elif link.find('artist') != -1:
            return self.Entity.Artist
        else:
            return None


if __name__ == '__main__':
    ym = YandexMusic()
    while True:
        query = input()
        name, _ = ym.search_artist_by_link(query)
        print(ym.search_artist(name))
