import spotipy
import yaml
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials

from common.music_service import MusicService


def validate_spotify_config(config):
    app_auth = config.get('app_auth')
    client_id = config.get('client_id')
    client_secret = config.get('client_secret')
    if app_auth is None:
        return False, 'Missing "app_auth" in spotify config'
    elif not app_auth:
        return False, 'Missing "app_auth" is "False"'
    else:
        if client_id is None:
            return False, 'Missing "client_id" in spotify config'
        elif client_secret is None:
            return False, 'Missing "client_secret" in spotify config'

    return True, None


class Spotify(MusicService):
    name = 'Spotify'

    def __init__(self, config):
        super(Spotify, self).__init__()

        self.client = None
        result, message = validate_spotify_config(config)
        if not result:
            raise ValueError(message)
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config['client_id'],
                                                                            client_secret=config['client_secret']))

    def search_track_by_link(self, link):
        try:
            track_info = self.client.track(link, market='RU')
            track = track_info['name']
            artists = [artist['name'] for artist in track_info['artists']]
            album = track_info['album']['name']
            return track, artists, album, self._get_entity_id(track_info['id'], self.Entity.Track)
        except SpotifyException:
            return None

    def search_track(self, track, artists, album=None):
        query = ', '.join(artists) + " - " + track
        results = self.client.search(q=query, type='track', market='RU')
        tracks_items = results['tracks']['items']
        if len(tracks_items) != 0:
            return tracks_items[0]['external_urls']['spotify']
        return None

    def search_track_by_query(self, query, limit=None):
        if not limit:
            limit = self.default_limit
        results = self.client.search(q=query, type='track', market='RU')
        tracks = results['tracks']['items'][:limit]
        track_list = []
        for track in tracks:
            track_list.append({
                'track': track['name'],
                'album': track['album']['name'],
                'artists': [artist['name'] for artist in track['artists']],
                'url': track['external_urls']['spotify']
            })
        response = {
            'service_name': self.name,
            'tracks': track_list
        }
        return response

    def search_artist_by_link(self, link):
        try:
            artist_info = self.client.artist(link)
            artist = artist_info['name']
            return artist, self._get_entity_id(artist_info['id'], self.Entity.Artist)
        except SpotifyException:
            return None

    def search_album_by_link(self, link):
        try:
            album_info = self.client.album(link)
            album = album_info['name']
            return album, self._get_entity_id(album_info['id'], self.Entity.Album)
        except SpotifyException:
            return None

    def search_artist(self, name):
        results = self.client.search(q=name, type='artist', market='RU')
        if results.get('artists'):
            if results['artists'].get('items'):
                if len(results['artists']['items']) > 0:
                    return results['artists']['items'][0]['external_urls']['spotify']
        return None

    def search_album(self, name):
        results = self.client.search(q=name, type='album', market='RU')
        if results.get('albums'):
            if results['albums'].get('items'):
                if len(results['albums']['items']) > 0:
                    return results['albums']['items'][0]['external_urls']['spotify']
        return None

    def detect_entity_by_link(self, link):
        if link.find("track") != -1:
            return self.Entity.Track
        elif link.find('album') != -1:
            return self.Entity.Album
        elif link.find('artist') != -1:
            return self.Entity.Artist
        else:
            return None

    @staticmethod
    def _entity_type_to_string(entity: MusicService.Entity):
        if entity == MusicService.Entity.Album:
            return "album"
        elif entity == MusicService.Entity.Track:
            return "track"
        elif entity == MusicService.Entity.Artist:
            return "artist"
        else:
            return None

    @staticmethod
    def _extract_track_data(track_json):
        return {
            'track': track_json['name'],
            'album': track_json['album']['name'],
            'artists': [artist['name'] for artist in track_json['artists']],
            'url': track_json['external_urls']['spotify']
        }

    @staticmethod
    def _extract_album_data(album_json):
        return {
            'album': album_json['name'],
            'artists': [artist['name'] for artist in album_json['artists']],
            'url': album_json['external_urls']['spotify']
        }

    @staticmethod
    def _extract_artist_data(artist_json):
        return {
            'artist': artist_json['name'],
            'url': artist_json['external_urls']['spotify']
        }

    @staticmethod
    def _extract_search_data(data_json, entity):
        if entity == MusicService.Entity.Album:
            return Spotify._extract_album_data(data_json)
        elif entity == MusicService.Entity.Track:
            return Spotify._extract_track_data(data_json)
        elif entity == MusicService.Entity.Artist:
            return Spotify._extract_artist_data(data_json)
        else:
            return None

    def search_by_query(self, query, entity: MusicService.Entity, limit=MusicService.default_limit):
        entity_str = self._entity_type_to_string(entity)
        if not entity_str:
            return None
        plural_entity_str = entity_str + "s"
        entity_list = []
        remaining_count = limit
        offset = 0
        while remaining_count > 0:
            results = self.client.search(q=query, type=entity_str, market='RU', offset=offset)
            results = results[plural_entity_str]['items'][:remaining_count]
            if len(results) == 0:
                break
            for result in results:
                entity_list.append(self._extract_search_data(result, entity))
                remaining_count -= 1
                offset += 1
        response = {
            'service_name': self.name,
            plural_entity_str: entity_list
        }
        return response


if __name__ == '__main__':
    config_filepath = "../config.yaml"
    with open(config_filepath, "r") as f:
        try:
            config = yaml.safe_load(f)
            sp = Spotify(config['spotify'])
            print(sp.search_by_query("three days grace", MusicService.Entity.Artist, 25))
            print(sp.search_by_query("love", MusicService.Entity.Track))
            print(sp.search_by_query("lov1e", MusicService.Entity.Album))
            print(sp.search_by_query("love", MusicService.Entity.Album))
            print(sp.client.track("https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx", market='RU'))
            print(sp.search_track_by_link("https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"))
            test_artists = ['Three Days Grace']
            test_track = 'I Hate Everything About You'
            test_query = ', '.join(test_artists) + " - " + test_track
            print(test_query)
            print(sp.client.search(q=test_query, type='track', market='RU'))
            print(sp.search_track(test_track, test_artists))
            print(sp.search_track_by_query(test_query, 2))
            link = "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
            print(sp.client.artist(link))
            print(sp.search_artist_by_link(link))
            link = "https://open.spotify.com/album/13topfW33NjnACjnRiZBX7"
            print(sp.client.album(link))
            print(sp.search_album_by_link(link))
            name = "Linkin Park"
            print(sp.client.search(name, type='artist', market='RU'))
            print(sp.search_artist(name))
            name = "Meteora"
            print(sp.client.search(name, type='album', market='RU'))
            print(sp.search_album(name))
            print(" ")
            print(sp.search_by_query("PVRIS", MusicService.Entity.Artist))
        except yaml.YAMLError as exc:
            print(exc)
