from common.music_service import MusicService
import requests
import re


class AppleMusic(MusicService):
    name = 'AppleMusic'

    # https://music.apple.com/ru/album/more-feat-lexie-liu-jaira-burns-seraphine-league-of-legends/1535612019?i=1535612021
    # https://music.apple.com/ru/album/fxxker/1203189772?i=1203189778
    # regex:
    # ((http|https)://)?(www\.)?music\.apple\.com/\w{2}/album/[^/]+/([0-9]+)\?i=([0-9]+)
    url_regex = re.compile(r'((http|https)://)?(www\.)?music\.apple\.com/\w{2}/album/[^/]+/([0-9]+)\?i=([0-9]+)')

    def __init__(self):
        super(AppleMusic, self).__init__()

    @staticmethod
    def _get_track_id_from_url(url):
        match = AppleMusic.url_regex.match(url)
        if match:
            return match[5]
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
        return track, artists, album, track_id

    def search_track(self, track, artists=None, album=None):
        query = track

        artists_exist = False
        album_exist = False

        if not artists is None:
            artists_exist = True
            query = ', '.join(artists) + " - " + track
        if not album is None:
            album_exist = True
            query = track + " " + album
        if artists_exist and album_exist:
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

    def search_track_by_query(self, query):
        raise NotImplemented()


if __name__ == '__main__':
    url = 'https://music.apple.com/ru/album/pop-stars-feat-jaira-burns/1439420228?i=1439420504'
    am = AppleMusic()
    track, artists, album, _ = am.search_track_by_link(url)
    print(am.search_track(track, artists, album))
