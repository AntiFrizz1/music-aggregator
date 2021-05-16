import re
import requests
from common.music_service import MusicService


class AppleMusic(MusicService):
    name = 'AppleMusic'

    # https://music.apple.com/ru/album/more-feat-lexie-liu-jaira-burns-seraphine-league-of-legends/1535612019?i=1535612021
    # https://music.apple.com/ru/album/fxxker/1203189772?i=1203189778
    url_regex = re.compile(r'((http|https)://)?(www\.)?music\.apple\.com/\w{2}/album/[^/]+/([0-9]+)\?i=([0-9]+)')
    # https://music.apple.com/us/artist/olivia-rodrigo/979458609
    url_artist_regex = re.compile(r'((http|https)://)?(www\.)?music\.apple\.com/\w{2}/artist/[^/]+/([0-9]+)')
    # https://music.apple.com/us/album/sour/1560735414
    url_album_regex = re.compile(r'((http|https)://)?(www\.)?music\.apple\.com/\w{2}/album/[^/]+/([0-9]+)')

    def __init__(self):
        super(AppleMusic, self).__init__()

    @staticmethod
    def _get_track_id_from_url(url):
        match = AppleMusic.url_regex.match(url)
        if match:
            return match[5]
        else:
            return None

    @staticmethod
    def _get_album_id_from_url(url):
        match = AppleMusic.url_album_regex.match(url)
        if match:
            return match[4]
        else:
            return None

    @staticmethod
    def _get_artist_id_from_url(url):
        match = AppleMusic.url_artist_regex.match(url)
        if match:
            return match[4]
        else:
            return None

    def search_track_by_link(self, link):
        track_id = self._get_track_id_from_url(link)
        if not track_id:
            return None
        url = 'https://itunes.apple.com/lookup'
        rsp = requests.get(url, params={
            'id': track_id,
            'entity': 'song',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None

        track_json = rsp_json['results'][0]
        track = track_json['trackName']
        artists = [track_json['artistName']]
        album = track_json['collectionName']
        return track, artists, album, self._get_entity_id(track_id, self.Entity.Track)

    def search_track(self, track, artists, album=None):
        query = ', '.join(artists) + " - " + track

        url = 'https://itunes.apple.com/search'
        rsp = requests.get(url, params={
            'term': query,
            'entity': 'song',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None

        track_url = rsp_json['results'][0]['trackViewUrl']
        return track_url

    def search_artist_by_link(self, link):
        artist_id = self._get_artist_id_from_url(link)
        if not artist_id:
            return None
        url = 'https://itunes.apple.com/lookup'
        rsp = requests.get(url, params={
            'id': artist_id,
            'entity': 'musicArtist',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None

        artist_json = rsp_json['results'][0]
        name = artist_json['artistName']
        return name, self._get_entity_id(artist_id, self.Entity.Artist)

    def search_artist(self, name):
        url = 'https://itunes.apple.com/search'
        rsp = requests.get(url, params={
            'term': name,
            'entity': 'musicArtist',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None

        artist_url = rsp_json['results'][0]['artistLinkUrl']
        return artist_url

    def search_album_by_link(self, link):
        album_id = self._get_album_id_from_url(link)
        if not album_id:
            return None
        url = 'https://itunes.apple.com/lookup'
        rsp = requests.get(url, params={
            'id': album_id,
            'entity': 'album',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None

        album_json = rsp_json['results'][0]
        name = album_json['collectionName']
        return name, self._get_entity_id(album_id, self.Entity.Album)

    def search_album(self, name):
        url = 'https://itunes.apple.com/search'
        rsp = requests.get(url, params={
            'term': name,
            'entity': 'album',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None

        album_url = rsp_json['results'][0]['collectionViewUrl']
        return album_url

    def detect_entity_by_link(self, link):
        if link.find("artist") != -1:
            return self.Entity.Artist
        elif self._get_track_id_from_url(link):
            return self.Entity.Track
        elif link.find('album') != -1:
            return self.Entity.Album
        else:
            return None

    def search_track_by_query(self, query, limit=None):
        if not limit:
            limit = self.default_limit
        url = 'https://itunes.apple.com/search'
        rsp = requests.get(url, params={
            'term': query,
            'entity': 'song',
            'country': 'RU'
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None
        tracks = rsp_json['results'][:limit]
        track_list = []
        for track in tracks:
            track_list.append({
                'track': track['trackName'],
                'album': track['collectionName'],
                'artists': [track['artistName']],
                'url': track['trackViewUrl']
            })
        response = {
            'service_name': self.name,
            'tracks': track_list
        }
        return response

    @staticmethod
    def _entity_type_to_string(entity: MusicService.Entity):
        if entity == MusicService.Entity.Album:
            return "album"
        elif entity == MusicService.Entity.Track:
            return "song"
        elif entity == MusicService.Entity.Artist:
            return "musicArtist"
        else:
            return None

    @staticmethod
    def _extract_track_data(track_json):
        return {
            'track': track_json['trackName'],
            'album': track_json['collectionName'],
            'artists': [track_json['artistName']],
            'url': track_json['trackViewUrl']
        }

    @staticmethod
    def _extract_album_data(album_json):
        return {
            'album': album_json['collectionName'],
            'artists': [album_json['artistName']],
            'url': album_json['collectionViewUrl']
        }

    @staticmethod
    def _extract_artist_data(artist_json):
        return {
            'artist': artist_json['artistName'],
            'url': artist_json['artistLinkUrl']
        }

    @staticmethod
    def _extract_search_data(data_json, entity):
        if entity == MusicService.Entity.Album:
            return AppleMusic._extract_album_data(data_json)
        elif entity == MusicService.Entity.Track:
            return AppleMusic._extract_track_data(data_json)
        elif entity == MusicService.Entity.Artist:
            return AppleMusic._extract_artist_data(data_json)
        else:
            return None

    def search_by_query(self, query, entity: MusicService.Entity, limit=MusicService.default_limit):
        entity_str = self._entity_type_to_string(entity)
        if not entity_str:
            return None
        url = 'https://itunes.apple.com/search'
        rsp = requests.get(url, params={
            'term': query,
            'entity': entity_str,
            'country': 'RU',
            'limit': limit
        })
        if rsp.status_code != 200:
            return None
        rsp_json = rsp.json()
        if rsp_json['resultCount'] == 0:
            return None
        results = rsp_json['results'][:limit]
        entity_list = []
        for result in results:
            entity_list.append(self._extract_search_data(result, entity))
        entity_plural_name = MusicService._entity_to_plural_str(entity)
        if not entity_plural_name:
            return None
        response = {
            'service_name': self.name,
            entity_plural_name: entity_list
        }
        return response


if __name__ == '__main__':
    am = AppleMusic()
    print(am.search_by_query("lil", MusicService.Entity.Artist))
    print(am.search_by_query("love", MusicService.Entity.Album))
    print(am.search_by_query("lil", MusicService.Entity.Track))
