import spotipy
from common.music_service import MusicService
from spotipy.oauth2 import SpotifyClientCredentials
import re
import logging
import yaml
from enum import Enum


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


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
                    filename="music-aggregator.log")


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
        self.spotify_url_link_regex = re.compile(r"((http|https)://)?(www\.)?open\.spotify\.com/track/(\w+)(\?.*)?")
        self.spotify_uri_regex = re.compile(r'spotify:track:(\w+)')

    @staticmethod
    def get_track_id_from_url_link_match(match):
        return match[4]

    @staticmethod
    def get_track_id_from_uri_link_match(match):
        return match[1]

    def get_track_id_from_link(self, link):
        match = self.spotify_url_link_regex.match(link)
        if not match is None:
            return self.get_track_id_from_url_link_match(match)
        match = self.spotify_uri_regex.match(link)
        if not match is None:
            return self.get_track_id_from_uri_link_match(match)
        return None

    # url types:
    # * https://open.spotify.com/track/30lo6PJqijZWV5sw8cDxcc?si=fZeJ0PtdRDSXDNNcWYF4mg
    # . regex: r'((http|https)://)?(www\.)?open\.spotify\.com/track/(\w+)(\?.*)?'
    # * spotify:track:30lo6PJqijZWV5sw8cDxcc
    # . regex: r'spotify:track:(\w+)'
    def search_track_by_link(self, link):
        track_id = self.get_track_id_from_link(link)
        if track_id is None:
            return None
        track_info = self.client.track(track_id, market='RU')
        track = track_info['name']
        artists = [artist['name'] for artist in track_info['artists']]
        album = track_info['album']['name']
        logging.debug((track, artists, album))
        return track, artists, album, track_id

    def search_track(self, track, artists=None, album=None):
        # queries = ["track:" + track]
        queries = [track]

        artists_exist = False
        album_exist = False

        if not artists is None:
            artists_exist = True
            # queries.append(track + " artist:" + ' '.join(artists))
            queries.append(', '.join(artists) + " - " + track)
        # if not album is None:
        #     album_exist = True
        #     queries.append("track:" + track + " album:" + album)
        # if artists_exist and album_exist:
        #     queries.append("track:" + track + " artist:" + ','.join(artists) + " album:" + album)

        search_response = []

        for query in queries:
            results = self.client.search(q=query, type='track', market='RU')
            search_response.append(results['tracks']['items'])
        for response in reversed(search_response):
            if len(response) != 0:
                return response[0]['external_urls']['spotify']
        return None

    def search_track_by_query(self, query, limit=None):
        if not limit:
            limit = self.default_limit
        results = self.client.search(q=query, type='track', market='RU')
        tracks = results['tracks']['items'][:limit]
        # tracks_urls = [track['external_urls']['spotify'] for track in tracks]
        # tracks_artists = [[artist['name'] for artist in track['artists']] for track in tracks]
        # tracks_name = [track['name'] for track in tracks]
        # tracks_album = [track['album']['name'] for track in tracks]
        # return list(zip(tracks_name, tracks_artists, tracks_album, tracks_urls))
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
        artist_info = self.client.artist(link)
        artist = artist_info['name']
        return artist, 'artist' + artist_info['id']

    def search_album_by_link(self, link):
        album_info = self.client.album(link)
        album = album_info['name']
        return album, 'album' + album_info['id']

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

    def search_by_link(self, link):
        if link.find("track") != -1:
            return self.search_track_by_link(link)
        elif link.find("artist") != -1:
            return self.search_artist(link)
        elif link.find("album") != -1:
            return self.search_album(link)
        else:
            return None


if __name__ == '__main__':
    config_filepath = "../config.yaml"
    with open(config_filepath, "r") as f:
        try:
            config = yaml.safe_load(f)
            spotify_client = Spotify(config['spotify'])
            while True:
                link = input()
                print(spotify_client.search_by_link(link))
                # name, id = spotify_client.search_album_by_link(link)
                # print(spotify_client.search_album(name))
        except yaml.YAMLError as exc:
            print(exc)
