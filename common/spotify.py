import re
import yaml

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import SpotifyException
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
