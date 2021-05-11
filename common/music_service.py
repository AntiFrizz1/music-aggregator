from enum import Enum


class MusicService:
    name = "MusicService"
    default_limit = 5

    class Entity(Enum):
        Track = 0
        Artist = 1
        Album = 2

    def _get_entity_id(self, entity_id, entity):
        return "%sq%sq%s" % (self.name, entity.name, entity_id)

    @staticmethod
    def _entity_to_plural_str(entity):
        if entity == MusicService.Entity.Track:
            return "tracks"
        elif entity == MusicService.Entity.Album:
            return "albums"
        elif entity == MusicService.Entity.Artist:
            return "artists"
        else:
            return None

    def detect_entity_by_link(self, link):
        raise NotImplemented

    def search_track_by_link(self, link):
        raise NotImplemented()

    def search_track(self, track, artists, album=None):
        raise NotImplemented()

    def search_track_by_query(self, query, limit=default_limit):
        raise NotImplemented()

    def search_by_query(self, query, entity: Entity, limit=default_limit):
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
        entity = self.detect_entity_by_link(link)
        if entity == self.Entity.Album:
            return self.search_album_by_link(link), entity
        elif entity == self.Entity.Artist:
            return self.search_artist_by_link(link), entity
        elif entity == self.Entity.Track:
            return self.search_track_by_link(link), entity
        return None

    def search_by_entity(self, entity, args):
        if entity == self.Entity.Album:
            return self.search_album(*args)
        elif entity == self.Entity.Artist:
            return self.search_artist(*args)
        elif entity == self.Entity.Track:
            return self.search_track(*args)
        return None
