class MusicService:
    name = "MusicService"
    default_limit = 5

    def search_track_by_link(self, link):
        raise NotImplemented()

    def search_track(self, track, artists=None, album=None):
        raise NotImplemented()

    def search_track_by_query(self, query):
        raise NotImplemented()

    def search_artist_by_link(self, link):
        raise NotImplemented()

    def search_artist(self, name):
        raise NotImplemented()

    def search_album_by_link(self, link):
        raise NotImplemented()

    def search_album(self, name):
        raise NotImplemented()

    def search_by_link(self, link):
        raise NotImplemented()
