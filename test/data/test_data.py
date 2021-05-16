# PLAYLISTS API
playlist_data = {
    "name": "Pop Music 2008",
    "description": "some popular music",
    "tracks": [
        {
            "service_name": "service1",
            "album": "Album1",
            "artists": [
                "Artist1",
                "Artist2"
            ],
            "track": "Best track 1",
            "url": "https://open.spotify.com/track/track_id"
        },
        {
            "service_name": "service2",
            "album": "Album2",
            "artists": [
                "Artist1",
                "Artist2",
                "Artist3"
            ],
            "track": "Best track 2",
            "url": "https://music.yandex.ru/album/abum_id/track/track_id"
        }
    ]
}

# SPOTIFY
spotify_test_track_link = "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"

spotify_api_search_track_by_link_result_json = {
    "album": {
        "album_type": "album",
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                },
                "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                "id": "2xiIXseIJcq3nG7C8fHeBj",
                "name": "Three Days Grace",
                "type": "artist",
                "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
            }
        ],
        "external_urls": {
            "spotify": "https://open.spotify.com/album/38pfSOHvxHqDWwDnjZ25U5"
        },
        "href": "https://api.spotify.com/v1/albums/38pfSOHvxHqDWwDnjZ25U5",
        "id": "38pfSOHvxHqDWwDnjZ25U5",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab67616d0000b273d3f7fc260cd67d23844ce2c0",
                "width": 640
            },
            {
                "height": 300,
                "url": "https://i.scdn.co/image/ab67616d00001e02d3f7fc260cd67d23844ce2c0",
                "width": 300
            },
            {
                "height": 64,
                "url": "https://i.scdn.co/image/ab67616d00004851d3f7fc260cd67d23844ce2c0",
                "width": 64
            }
        ],
        "name": "Three Days Grace (Deluxe Version)",
        "release_date": "2007-12-25",
        "release_date_precision": "day",
        "total_tracks": 15,
        "type": "album",
        "uri": "spotify:album:38pfSOHvxHqDWwDnjZ25U5"
    },
    "artists": [
        {
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
            },
            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
            "id": "2xiIXseIJcq3nG7C8fHeBj",
            "name": "Three Days Grace",
            "type": "artist",
            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
        }
    ],
    "disc_number": 1,
    "duration_ms": 231480,
    "explicit": False,
    "external_ids": {
        "isrc": "USJI10300075"
    },
    "external_urls": {
        "spotify": "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
    },
    "href": "https://api.spotify.com/v1/tracks/6rUp7v3l8yC4TKxAAR5Bmx",
    "id": "6rUp7v3l8yC4TKxAAR5Bmx",
    "is_local": False,
    "is_playable": True,
    "name": "I Hate Everything About You",
    "popularity": 73,
    "preview_url": "https://p.scdn.co/mp3-preview/8893669447625edf76339cdd67a338dad034a7ea?cid=2f1bc82113914f19a1cc66af6caa2cfc",
    "track_number": 3,
    "type": "track",
    "uri": "spotify:track:6rUp7v3l8yC4TKxAAR5Bmx"
}

spotify_api_search_track_result_json = {
    "tracks": {
        "href": "https://api.spotify.com/v1/search?query=Three+Days+Grace+-+I+Hate+Everything+About+You&type=track&market=RU&offset=0&limit=10",
        "items": [
            {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                            },
                            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                            "id": "2xiIXseIJcq3nG7C8fHeBj",
                            "name": "Three Days Grace",
                            "type": "artist",
                            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/38pfSOHvxHqDWwDnjZ25U5"
                    },
                    "href": "https://api.spotify.com/v1/albums/38pfSOHvxHqDWwDnjZ25U5",
                    "id": "38pfSOHvxHqDWwDnjZ25U5",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b273d3f7fc260cd67d23844ce2c0",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e02d3f7fc260cd67d23844ce2c0",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d00004851d3f7fc260cd67d23844ce2c0",
                            "width": 64
                        }
                    ],
                    "name": "Three Days Grace (Deluxe Version)",
                    "release_date": "2007-12-25",
                    "release_date_precision": "day",
                    "total_tracks": 15,
                    "type": "album",
                    "uri": "spotify:album:38pfSOHvxHqDWwDnjZ25U5"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 231480,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10300075"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
                },
                "href": "https://api.spotify.com/v1/tracks/6rUp7v3l8yC4TKxAAR5Bmx",
                "id": "6rUp7v3l8yC4TKxAAR5Bmx",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You",
                "popularity": 73,
                "preview_url": "https://p.scdn.co/mp3-preview/8893669447625edf76339cdd67a338dad034a7ea?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 3,
                "type": "track",
                "uri": "spotify:track:6rUp7v3l8yC4TKxAAR5Bmx"
            },
            {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                            },
                            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                            "id": "2xiIXseIJcq3nG7C8fHeBj",
                            "name": "Three Days Grace",
                            "type": "artist",
                            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/38pfSOHvxHqDWwDnjZ25U5"
                    },
                    "href": "https://api.spotify.com/v1/albums/38pfSOHvxHqDWwDnjZ25U5",
                    "id": "38pfSOHvxHqDWwDnjZ25U5",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b273d3f7fc260cd67d23844ce2c0",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e02d3f7fc260cd67d23844ce2c0",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d00004851d3f7fc260cd67d23844ce2c0",
                            "width": 64
                        }
                    ],
                    "name": "Three Days Grace (Deluxe Version)",
                    "release_date": "2007-12-25",
                    "release_date_precision": "day",
                    "total_tracks": 15,
                    "type": "album",
                    "uri": "spotify:album:38pfSOHvxHqDWwDnjZ25U5"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 236906,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10401012"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/4yRRrMzaXzXiCbbWrt5KDy"
                },
                "href": "https://api.spotify.com/v1/tracks/4yRRrMzaXzXiCbbWrt5KDy",
                "id": "4yRRrMzaXzXiCbbWrt5KDy",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You - Live Acoustic - Rolling Stone Original (EP)",
                "popularity": 43,
                "preview_url": "https://p.scdn.co/mp3-preview/a291243ea7b8499144fc2b8b3d3741d832929588?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 13,
                "type": "track",
                "uri": "spotify:track:4yRRrMzaXzXiCbbWrt5KDy"
            },
            {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                            },
                            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                            "id": "2xiIXseIJcq3nG7C8fHeBj",
                            "name": "Three Days Grace",
                            "type": "artist",
                            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/13topfW33NjnACjnRiZBX7"
                    },
                    "href": "https://api.spotify.com/v1/albums/13topfW33NjnACjnRiZBX7",
                    "id": "13topfW33NjnACjnRiZBX7",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b27377922eaa071fb388270f203f",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e0277922eaa071fb388270f203f",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d0000485177922eaa071fb388270f203f",
                            "width": 64
                        }
                    ],
                    "name": "Three Days Grace",
                    "release_date": "2003-04-19",
                    "release_date_precision": "day",
                    "total_tracks": 12,
                    "type": "album",
                    "uri": "spotify:album:13topfW33NjnACjnRiZBX7"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 231480,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10300075"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/0M955bMOoilikPXwKLYpoi"
                },
                "href": "https://api.spotify.com/v1/tracks/0M955bMOoilikPXwKLYpoi",
                "id": "0M955bMOoilikPXwKLYpoi",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You",
                "popularity": 72,
                "preview_url": "https://p.scdn.co/mp3-preview/8893669447625edf76339cdd67a338dad034a7ea?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 3,
                "type": "track",
                "uri": "spotify:track:0M955bMOoilikPXwKLYpoi"
            },
            {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                            },
                            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                            "id": "2xiIXseIJcq3nG7C8fHeBj",
                            "name": "Three Days Grace",
                            "type": "artist",
                            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/4zTqKv6iC5pMtAajRs2m7K"
                    },
                    "href": "https://api.spotify.com/v1/albums/4zTqKv6iC5pMtAajRs2m7K",
                    "id": "4zTqKv6iC5pMtAajRs2m7K",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b27325b37a022d79d156668e5fb4",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e0225b37a022d79d156668e5fb4",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d0000485125b37a022d79d156668e5fb4",
                            "width": 64
                        }
                    ],
                    "name": "I Hate Everything About You (Acoustic Version)",
                    "release_date": "2003-09-22",
                    "release_date_precision": "day",
                    "total_tracks": 1,
                    "type": "album",
                    "uri": "spotify:album:4zTqKv6iC5pMtAajRs2m7K"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 222653,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10301066"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/6XFDGxqrs7V2cKSjw1cv5B"
                },
                "href": "https://api.spotify.com/v1/tracks/6XFDGxqrs7V2cKSjw1cv5B",
                "id": "6XFDGxqrs7V2cKSjw1cv5B",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You - Acoustic Version",
                "popularity": 34,
                "preview_url": "https://p.scdn.co/mp3-preview/aff19f3b58e7d273e59cd4ded25f71ea6a1864ff?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 1,
                "type": "track",
                "uri": "spotify:track:6XFDGxqrs7V2cKSjw1cv5B"
            },
            {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                            },
                            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                            "id": "2xiIXseIJcq3nG7C8fHeBj",
                            "name": "Three Days Grace",
                            "type": "artist",
                            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/6S7lvN6dnZ7EU8TPujw7gd"
                    },
                    "href": "https://api.spotify.com/v1/albums/6S7lvN6dnZ7EU8TPujw7gd",
                    "id": "6S7lvN6dnZ7EU8TPujw7gd",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b273f84f503fbcacca302785b94a",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e02f84f503fbcacca302785b94a",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d00004851f84f503fbcacca302785b94a",
                            "width": 64
                        }
                    ],
                    "name": "Rolling Stone Original (EP)",
                    "release_date": "2003-07-22",
                    "release_date_precision": "day",
                    "total_tracks": 4,
                    "type": "album",
                    "uri": "spotify:album:6S7lvN6dnZ7EU8TPujw7gd"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 239680,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10401012"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/7e2073Iang0hKXlFoffwpF"
                },
                "href": "https://api.spotify.com/v1/tracks/7e2073Iang0hKXlFoffwpF",
                "id": "7e2073Iang0hKXlFoffwpF",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You - Live Acoustic - Rolling Stone Original (EP)",
                "popularity": 19,
                "preview_url": "https://p.scdn.co/mp3-preview/c598d06980413ca6561d9ebea08bf73e1bb1d710?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 4,
                "type": "track",
                "uri": "spotify:track:7e2073Iang0hKXlFoffwpF"
            },
            {
                "album": {
                    "album_type": "compilation",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of"
                            },
                            "href": "https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of",
                            "id": "0LyfQWJT6nXafLPZqxe9Of",
                            "name": "Various Artists",
                            "type": "artist",
                            "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/1t987QQUIfdOwcCTI25j6J"
                    },
                    "href": "https://api.spotify.com/v1/albums/1t987QQUIfdOwcCTI25j6J",
                    "id": "1t987QQUIfdOwcCTI25j6J",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b273a72a36968ef25332ad07f932",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e02a72a36968ef25332ad07f932",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d00004851a72a36968ef25332ad07f932",
                            "width": 64
                        }
                    ],
                    "name": "Pure... Hard Rock",
                    "release_date": "2011-06-06",
                    "release_date_precision": "day",
                    "total_tracks": 68,
                    "type": "album",
                    "uri": "spotify:album:1t987QQUIfdOwcCTI25j6J"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 231320,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10300075"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/0iWMnHtF1EFfRIWTYfx7Wi"
                },
                "href": "https://api.spotify.com/v1/tracks/0iWMnHtF1EFfRIWTYfx7Wi",
                "id": "0iWMnHtF1EFfRIWTYfx7Wi",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You",
                "popularity": 19,
                "preview_url": "https://p.scdn.co/mp3-preview/47ac6065d405d9b4f5ef6cea48e954244b49d185?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 7,
                "type": "track",
                "uri": "spotify:track:0iWMnHtF1EFfRIWTYfx7Wi"
            },
            {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/6DwFwtsHLMGyXmry54SNPZ"
                            },
                            "href": "https://api.spotify.com/v1/artists/6DwFwtsHLMGyXmry54SNPZ",
                            "id": "6DwFwtsHLMGyXmry54SNPZ",
                            "name": "Midifine Systems",
                            "type": "artist",
                            "uri": "spotify:artist:6DwFwtsHLMGyXmry54SNPZ"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/2Q2XmlW61xDTJW3FOzqXJN"
                    },
                    "href": "https://api.spotify.com/v1/albums/2Q2XmlW61xDTJW3FOzqXJN",
                    "id": "2Q2XmlW61xDTJW3FOzqXJN",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b273c6be29771028ee0869c65090",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e02c6be29771028ee0869c65090",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d00004851c6be29771028ee0869c65090",
                            "width": 64
                        }
                    ],
                    "name": "Best for Musicians No. 819 (Karaoke Version)",
                    "release_date": "2014-04-16",
                    "release_date_precision": "day",
                    "total_tracks": 17,
                    "type": "album",
                    "uri": "spotify:album:2Q2XmlW61xDTJW3FOzqXJN"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/6DwFwtsHLMGyXmry54SNPZ"
                        },
                        "href": "https://api.spotify.com/v1/artists/6DwFwtsHLMGyXmry54SNPZ",
                        "id": "6DwFwtsHLMGyXmry54SNPZ",
                        "name": "Midifine Systems",
                        "type": "artist",
                        "uri": "spotify:artist:6DwFwtsHLMGyXmry54SNPZ"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 228112,
                "explicit": False,
                "external_ids": {
                    "isrc": "DESN31322992"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/2vPBkZqLG47j4Xvhiuog8X"
                },
                "href": "https://api.spotify.com/v1/tracks/2vPBkZqLG47j4Xvhiuog8X",
                "id": "2vPBkZqLG47j4Xvhiuog8X",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You (Originally Performed By Three Days Grace) - Karaoke Version",
                "popularity": 1,
                "preview_url": "https://p.scdn.co/mp3-preview/2b005d0f3977d4b0c0ce337cb79e496b83a4e992?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 7,
                "type": "track",
                "uri": "spotify:track:2vPBkZqLG47j4Xvhiuog8X"
            },
            {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/6aLDS9oOXpit8wJTtueP8g"
                            },
                            "href": "https://api.spotify.com/v1/artists/6aLDS9oOXpit8wJTtueP8g",
                            "id": "6aLDS9oOXpit8wJTtueP8g",
                            "name": "Ameritz - Karaoke",
                            "type": "artist",
                            "uri": "spotify:artist:6aLDS9oOXpit8wJTtueP8g"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/0j97Z3JcchBywcnn0DqPSg"
                    },
                    "href": "https://api.spotify.com/v1/albums/0j97Z3JcchBywcnn0DqPSg",
                    "id": "0j97Z3JcchBywcnn0DqPSg",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b273235c05ab08dd2bf752e164a4",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e02235c05ab08dd2bf752e164a4",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d00004851235c05ab08dd2bf752e164a4",
                            "width": 64
                        }
                    ],
                    "name": "Karaoke - In the Style of Three Days Grace",
                    "release_date": "2012-05-01",
                    "release_date_precision": "day",
                    "total_tracks": 5,
                    "type": "album",
                    "uri": "spotify:album:0j97Z3JcchBywcnn0DqPSg"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/6aLDS9oOXpit8wJTtueP8g"
                        },
                        "href": "https://api.spotify.com/v1/artists/6aLDS9oOXpit8wJTtueP8g",
                        "id": "6aLDS9oOXpit8wJTtueP8g",
                        "name": "Ameritz - Karaoke",
                        "type": "artist",
                        "uri": "spotify:artist:6aLDS9oOXpit8wJTtueP8g"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 229095,
                "explicit": False,
                "external_ids": {
                    "isrc": "USA561218062"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/7Jfkv4U3qRAVtOzVjZyhe2"
                },
                "href": "https://api.spotify.com/v1/tracks/7Jfkv4U3qRAVtOzVjZyhe2",
                "id": "7Jfkv4U3qRAVtOzVjZyhe2",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You (In the Style of Three Days Grace) [Karaoke Version]",
                "popularity": 0,
                "preview_url": "https://p.scdn.co/mp3-preview/67ad237b3c16692ceb2e36bddd4d369bdd58f6d1?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 2,
                "type": "track",
                "uri": "spotify:track:7Jfkv4U3qRAVtOzVjZyhe2"
            },
            {
                "album": {
                    "album_type": "single",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                            },
                            "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                            "id": "2xiIXseIJcq3nG7C8fHeBj",
                            "name": "Three Days Grace",
                            "type": "artist",
                            "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/4r0iCMWCP67obGWcADi3nj"
                    },
                    "href": "https://api.spotify.com/v1/albums/4r0iCMWCP67obGWcADi3nj",
                    "id": "4r0iCMWCP67obGWcADi3nj",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b27307ebc75f2c34011837b8c764",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e0207ebc75f2c34011837b8c764",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d0000485107ebc75f2c34011837b8c764",
                            "width": 64
                        }
                    ],
                    "name": "I Hate Everything About You",
                    "release_date": "2003-07-14",
                    "release_date_precision": "day",
                    "total_tracks": 2,
                    "type": "album",
                    "uri": "spotify:album:4r0iCMWCP67obGWcADi3nj"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                        },
                        "href": "https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                        "id": "2xiIXseIJcq3nG7C8fHeBj",
                        "name": "Three Days Grace",
                        "type": "artist",
                        "uri": "spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 231333,
                "explicit": False,
                "external_ids": {
                    "isrc": "USJI10300075"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/75QjgdQaW9XXAFwKVir5YR"
                },
                "href": "https://api.spotify.com/v1/tracks/75QjgdQaW9XXAFwKVir5YR",
                "id": "75QjgdQaW9XXAFwKVir5YR",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You",
                "popularity": 24,
                "preview_url": "https://p.scdn.co/mp3-preview/ff708e1fe1557c5e41fbaf056aad6b301ce47436?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 1,
                "type": "track",
                "uri": "spotify:track:75QjgdQaW9XXAFwKVir5YR"
            },
            {
                "album": {
                    "album_type": "album",
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/5UloVKzUNJcjORzhhTWWiJ"
                            },
                            "href": "https://api.spotify.com/v1/artists/5UloVKzUNJcjORzhhTWWiJ",
                            "id": "5UloVKzUNJcjORzhhTWWiJ",
                            "name": "The Karaoke Channel",
                            "type": "artist",
                            "uri": "spotify:artist:5UloVKzUNJcjORzhhTWWiJ"
                        }
                    ],
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/6O3mH7ujgES5PWSAasUZHE"
                    },
                    "href": "https://api.spotify.com/v1/albums/6O3mH7ujgES5PWSAasUZHE",
                    "id": "6O3mH7ujgES5PWSAasUZHE",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/ab67616d0000b2735b747cda942562cceb11f1c2",
                            "width": 640
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/ab67616d00001e025b747cda942562cceb11f1c2",
                            "width": 300
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/ab67616d000048515b747cda942562cceb11f1c2",
                            "width": 64
                        }
                    ],
                    "name": "Karaoke - In The Style Of Three Days Grace - Vol. 1",
                    "release_date": "2008-01-15",
                    "release_date_precision": "day",
                    "total_tracks": 10,
                    "type": "album",
                    "uri": "spotify:album:6O3mH7ujgES5PWSAasUZHE"
                },
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/5UloVKzUNJcjORzhhTWWiJ"
                        },
                        "href": "https://api.spotify.com/v1/artists/5UloVKzUNJcjORzhhTWWiJ",
                        "id": "5UloVKzUNJcjORzhhTWWiJ",
                        "name": "The Karaoke Channel",
                        "type": "artist",
                        "uri": "spotify:artist:5UloVKzUNJcjORzhhTWWiJ"
                    }
                ],
                "disc_number": 1,
                "duration_ms": 228048,
                "explicit": False,
                "external_ids": {
                    "isrc": "USK4W0719990"
                },
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/6Hlb6GtXHxeL5mOyj5lRZt"
                },
                "href": "https://api.spotify.com/v1/tracks/6Hlb6GtXHxeL5mOyj5lRZt",
                "id": "6Hlb6GtXHxeL5mOyj5lRZt",
                "is_local": False,
                "is_playable": True,
                "name": "I Hate Everything About You - Composed Or Made Famous By Three Days Grace",
                "popularity": 0,
                "preview_url": "https://p.scdn.co/mp3-preview/d83bfffb455603b01ee3fadaabcfd9f4d4248278?cid=2f1bc82113914f19a1cc66af6caa2cfc",
                "track_number": 1,
                "type": "track",
                "uri": "spotify:track:6Hlb6GtXHxeL5mOyj5lRZt"
            }
        ],
        "limit": 10,
        "next": "https://api.spotify.com/v1/search?query=Three+Days+Grace+-+I+Hate+Everything+About+You&type=track&market=RU&offset=10&limit=10",
        "offset": 0,
        "previous": "None",
        "total": 19
    }
}