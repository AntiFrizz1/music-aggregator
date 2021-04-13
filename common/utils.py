from transliterate import translit
from name_map import name_map

def custom_translit(s, lang, reversed=False):
    if name_map.get(s) is None:
        return translit(s, lang, reversed=reversed)
    else:
        return name_map[s]


def is_artists_equal(artists, expected_artists):
    is_equal = True
    # print(artists, expected_artists)
    for artist in artists:
        f = False
        for expected_artist in expected_artists:
            # print(artist, custom_translit(artist, 'ru', reversed=True), custom_translit(artist, 'ru'), expected_artist, custom_translit(expected_artist, 'ru', reversed=True), custom_translit(expected_artist, 'ru'))
            if artist.upper() == expected_artist.upper() or \
               custom_translit(artist, 'ru', reversed=True).upper() == expected_artist.upper() or \
               custom_translit(artist, 'ru').upper() == expected_artist.upper() or \
               artist.upper() == custom_translit(expected_artist, 'ru', reversed=True).upper() or \
               artist.upper() == custom_translit(expected_artist, 'ru').upper():
                f = True
                break
        if not f:
            is_equal = False
            break
    return is_equal

def is_equal(items, expected_items):
    # print(items, expected_items)
    for item in items:
        for expected_item in expected_items:
            if item.upper() == expected_item.upper():
                return True
    return False