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

spotify_api_search_track_by_query_extracted_result_with_limit_2 = {
   "service_name":"Spotify",
   "tracks":[
      {
         "track":"I Hate Everything About You",
         "album":"Three Days Grace (Deluxe Version)",
         "artists":[
            "Three Days Grace"
         ],
         "url":"https://open.spotify.com/track/6rUp7v3l8yC4TKxAAR5Bmx"
      },
      {
         "track":"I Hate Everything About You - Live Acoustic - Rolling Stone Original (EP)",
         "album":"Three Days Grace (Deluxe Version)",
         "artists":[
            "Three Days Grace"
         ],
         "url":"https://open.spotify.com/track/4yRRrMzaXzXiCbbWrt5KDy"
      }
   ]
}

spotify_test_artist_tdg = {
   "external_urls":{
      "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
   },
   "followers":{
      "href":"None",
      "total":4481680
   },
   "genres":[
      "alternative metal",
      "canadian metal",
      "canadian rock",
      "nu metal",
      "post-grunge"
   ],
   "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
   "id":"2xiIXseIJcq3nG7C8fHeBj",
   "images":[
      {
         "height":640,
         "url":"https://i.scdn.co/image/2a9ec8d494f8d0a52fd67c3239efc2b9e79a4ced",
         "width":640
      },
      {
         "height":320,
         "url":"https://i.scdn.co/image/4d8741f7fca53b7b1ff9d6d6b1176420df7e8200",
         "width":320
      },
      {
         "height":160,
         "url":"https://i.scdn.co/image/aaeae81ffa892a04619203bfbab22ad0582c2e9d",
         "width":160
      }
   ],
   "name":"Three Days Grace",
   "popularity":79,
   "type":"artist",
   "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
}

spotify_test_album_tdg = {
   "album_type":"album",
   "artists":[
      {
         "external_urls":{
            "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
         },
         "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
         "id":"2xiIXseIJcq3nG7C8fHeBj",
         "name":"Three Days Grace",
         "type":"artist",
         "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
      }
   ],
   "available_markets":[
      "AD",
      "AE",
      "AG",
      "AL",
      "AM",
      "AO",
      "AR",
      "AT",
      "AU",
      "AZ",
      "BA",
      "BB",
      "BD",
      "BE",
      "BF",
      "BG",
      "BH",
      "BI",
      "BJ",
      "BN",
      "BO",
      "BR",
      "BS",
      "BT",
      "BW",
      "BY",
      "BZ",
      "CA",
      "CH",
      "CI",
      "CL",
      "CM",
      "CO",
      "CR",
      "CV",
      "CW",
      "CY",
      "CZ",
      "DE",
      "DJ",
      "DK",
      "DM",
      "DO",
      "DZ",
      "EC",
      "EE",
      "EG",
      "ES",
      "FI",
      "FJ",
      "FM",
      "FR",
      "GA",
      "GB",
      "GD",
      "GE",
      "GH",
      "GM",
      "GN",
      "GQ",
      "GR",
      "GT",
      "GW",
      "GY",
      "HN",
      "HR",
      "HT",
      "HU",
      "ID",
      "IE",
      "IL",
      "IN",
      "IS",
      "IT",
      "JM",
      "JO",
      "JP",
      "KE",
      "KG",
      "KH",
      "KI",
      "KM",
      "KN",
      "KR",
      "KW",
      "KZ",
      "LA",
      "LB",
      "LC",
      "LI",
      "LK",
      "LR",
      "LS",
      "LT",
      "LU",
      "LV",
      "MA",
      "MC",
      "MD",
      "ME",
      "MG",
      "MH",
      "MK",
      "ML",
      "MN",
      "MR",
      "MT",
      "MU",
      "MV",
      "MW",
      "MX",
      "MY",
      "MZ",
      "NA",
      "NE",
      "NG",
      "NI",
      "NL",
      "NO",
      "NP",
      "NR",
      "NZ",
      "OM",
      "PA",
      "PE",
      "PG",
      "PH",
      "PK",
      "PL",
      "PS",
      "PT",
      "PW",
      "PY",
      "QA",
      "RO",
      "RS",
      "RU",
      "RW",
      "SA",
      "SB",
      "SC",
      "SE",
      "SG",
      "SI",
      "SK",
      "SL",
      "SM",
      "SN",
      "SR",
      "ST",
      "SV",
      "SZ",
      "TD",
      "TG",
      "TH",
      "TL",
      "TN",
      "TO",
      "TT",
      "TV",
      "TW",
      "TZ",
      "UA",
      "UG",
      "US",
      "UY",
      "UZ",
      "VC",
      "VU",
      "WS",
      "XK",
      "ZA",
      "ZM",
      "ZW"
   ],
   "copyrights":[
      {
         "text":"(P) 2003 RCA/JIVE Label Group, a unit of Sony Music Entertainment",
         "type":"P"
      }
   ],
   "external_ids":{
      "upc":"828765347921"
   },
   "external_urls":{
      "spotify":"https://open.spotify.com/album/13topfW33NjnACjnRiZBX7"
   },
   "genres":[
      
   ],
   "href":"https://api.spotify.com/v1/albums/13topfW33NjnACjnRiZBX7",
   "id":"13topfW33NjnACjnRiZBX7",
   "images":[
      {
         "height":640,
         "url":"https://i.scdn.co/image/ab67616d0000b27377922eaa071fb388270f203f",
         "width":640
      },
      {
         "height":300,
         "url":"https://i.scdn.co/image/ab67616d00001e0277922eaa071fb388270f203f",
         "width":300
      },
      {
         "height":64,
         "url":"https://i.scdn.co/image/ab67616d0000485177922eaa071fb388270f203f",
         "width":64
      }
   ],
   "label":"Jive",
   "name":"Three Days Grace",
   "popularity":70,
   "release_date":"2003-04-19",
   "release_date_precision":"day",
   "total_tracks":12,
   "tracks":{
      "href":"https://api.spotify.com/v1/albums/13topfW33NjnACjnRiZBX7/tracks?offset=0&limit=50",
      "items":[
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":267173,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/4DmH8WEuvLOXpZ5D18XHJw"
            },
            "href":"https://api.spotify.com/v1/tracks/4DmH8WEuvLOXpZ5D18XHJw",
            "id":"4DmH8WEuvLOXpZ5D18XHJw",
            "is_local":False,
            "name":"Burn",
            "preview_url":"https://p.scdn.co/mp3-preview/247394fe55f02d3010d4652ad0b74cf16345ab6b?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":1,
            "type":"track",
            "uri":"spotify:track:4DmH8WEuvLOXpZ5D18XHJw"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":186893,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/0CA3RxBx2xSQXPfpmUBK1v"
            },
            "href":"https://api.spotify.com/v1/tracks/0CA3RxBx2xSQXPfpmUBK1v",
            "id":"0CA3RxBx2xSQXPfpmUBK1v",
            "is_local":False,
            "name":"Just Like You",
            "preview_url":"https://p.scdn.co/mp3-preview/1276a2b1f5aded2deaf36fcb2fc7bc4ac03e629a?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":2,
            "type":"track",
            "uri":"spotify:track:0CA3RxBx2xSQXPfpmUBK1v"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":231480,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/0M955bMOoilikPXwKLYpoi"
            },
            "href":"https://api.spotify.com/v1/tracks/0M955bMOoilikPXwKLYpoi",
            "id":"0M955bMOoilikPXwKLYpoi",
            "is_local":False,
            "name":"I Hate Everything About You",
            "preview_url":"https://p.scdn.co/mp3-preview/8893669447625edf76339cdd67a338dad034a7ea?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":3,
            "type":"track",
            "uri":"spotify:track:0M955bMOoilikPXwKLYpoi"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":260680,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/11RUCSAgpexhJSMmcuO4h2"
            },
            "href":"https://api.spotify.com/v1/tracks/11RUCSAgpexhJSMmcuO4h2",
            "id":"11RUCSAgpexhJSMmcuO4h2",
            "is_local":False,
            "name":"Home",
            "preview_url":"https://p.scdn.co/mp3-preview/2f0d1ad8882683c5c8d61a71c4281afee3bb62dd?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":4,
            "type":"track",
            "uri":"spotify:track:11RUCSAgpexhJSMmcuO4h2"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":193120,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/0OWmBvdthZceFMOwB5EANd"
            },
            "href":"https://api.spotify.com/v1/tracks/0OWmBvdthZceFMOwB5EANd",
            "id":"0OWmBvdthZceFMOwB5EANd",
            "is_local":False,
            "name":"Scared",
            "preview_url":"https://p.scdn.co/mp3-preview/9ab4b3b8d3e8d982ec2678b726db7df2221be0e3?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":5,
            "type":"track",
            "uri":"spotify:track:0OWmBvdthZceFMOwB5EANd"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":224520,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/4kW5sp3Ah4hS5mkArOJSyJ"
            },
            "href":"https://api.spotify.com/v1/tracks/4kW5sp3Ah4hS5mkArOJSyJ",
            "id":"4kW5sp3Ah4hS5mkArOJSyJ",
            "is_local":False,
            "name":"Let You Down",
            "preview_url":"https://p.scdn.co/mp3-preview/a5c4ce9b871b7e9bc3a61cc88f00600b9ce1d6fd?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":6,
            "type":"track",
            "uri":"spotify:track:4kW5sp3Ah4hS5mkArOJSyJ"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":180546,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/2Viqjkxmiu8hGIhjwtqYvI"
            },
            "href":"https://api.spotify.com/v1/tracks/2Viqjkxmiu8hGIhjwtqYvI",
            "id":"2Viqjkxmiu8hGIhjwtqYvI",
            "is_local":False,
            "name":"Now or Never",
            "preview_url":"https://p.scdn.co/mp3-preview/ce00359ce0ca68f07e0e0737f161a206d7ca2ef0?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":7,
            "type":"track",
            "uri":"spotify:track:2Viqjkxmiu8hGIhjwtqYvI"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":212386,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/3WmiisfwPICXyzJBrOSfI8"
            },
            "href":"https://api.spotify.com/v1/tracks/3WmiisfwPICXyzJBrOSfI8",
            "id":"3WmiisfwPICXyzJBrOSfI8",
            "is_local":False,
            "name":"Born Like This",
            "preview_url":"https://p.scdn.co/mp3-preview/d11cbb5a6d2a17c414e2029e08dedeaec06ae083?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":8,
            "type":"track",
            "uri":"spotify:track:3WmiisfwPICXyzJBrOSfI8"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":208493,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/2pVyreySMezcsVq0nmsIJ6"
            },
            "href":"https://api.spotify.com/v1/tracks/2pVyreySMezcsVq0nmsIJ6",
            "id":"2pVyreySMezcsVq0nmsIJ6",
            "is_local":False,
            "name":"Drown",
            "preview_url":"https://p.scdn.co/mp3-preview/ba977e56e0dfccd50084f889af61422b8d2e9801?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":9,
            "type":"track",
            "uri":"spotify:track:2pVyreySMezcsVq0nmsIJ6"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":204373,
            "explicit":True,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/57RstmiMTPQXUvx6O41ZC7"
            },
            "href":"https://api.spotify.com/v1/tracks/57RstmiMTPQXUvx6O41ZC7",
            "id":"57RstmiMTPQXUvx6O41ZC7",
            "is_local":False,
            "name":"Wake Up",
            "preview_url":"https://p.scdn.co/mp3-preview/9f9b198a6f6b26174534843cc292b2fb6800a0ce?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":10,
            "type":"track",
            "uri":"spotify:track:57RstmiMTPQXUvx6O41ZC7"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               "AD",
               "AE",
               "AG",
               "AL",
               "AM",
               "AO",
               "AR",
               "AT",
               "AU",
               "AZ",
               "BA",
               "BB",
               "BD",
               "BE",
               "BF",
               "BG",
               "BH",
               "BI",
               "BJ",
               "BN",
               "BO",
               "BR",
               "BS",
               "BT",
               "BW",
               "BY",
               "BZ",
               "CA",
               "CH",
               "CI",
               "CL",
               "CM",
               "CO",
               "CR",
               "CV",
               "CW",
               "CY",
               "CZ",
               "DE",
               "DJ",
               "DK",
               "DM",
               "DO",
               "DZ",
               "EC",
               "EE",
               "EG",
               "ES",
               "FI",
               "FJ",
               "FM",
               "FR",
               "GA",
               "GB",
               "GD",
               "GE",
               "GH",
               "GM",
               "GN",
               "GQ",
               "GR",
               "GT",
               "GW",
               "GY",
               "HN",
               "HR",
               "HT",
               "HU",
               "ID",
               "IE",
               "IL",
               "IN",
               "IS",
               "IT",
               "JM",
               "JO",
               "JP",
               "KE",
               "KG",
               "KH",
               "KI",
               "KM",
               "KN",
               "KR",
               "KW",
               "KZ",
               "LA",
               "LB",
               "LC",
               "LI",
               "LK",
               "LR",
               "LS",
               "LT",
               "LU",
               "LV",
               "MA",
               "MC",
               "MD",
               "ME",
               "MG",
               "MH",
               "MK",
               "ML",
               "MN",
               "MR",
               "MT",
               "MU",
               "MV",
               "MW",
               "MX",
               "MY",
               "MZ",
               "NA",
               "NE",
               "NG",
               "NI",
               "NL",
               "NO",
               "NP",
               "NR",
               "NZ",
               "OM",
               "PA",
               "PE",
               "PG",
               "PH",
               "PK",
               "PL",
               "PS",
               "PT",
               "PW",
               "PY",
               "QA",
               "RO",
               "RS",
               "RU",
               "RW",
               "SA",
               "SB",
               "SC",
               "SE",
               "SG",
               "SI",
               "SK",
               "SL",
               "SM",
               "SN",
               "SR",
               "ST",
               "SV",
               "SZ",
               "TD",
               "TG",
               "TH",
               "TL",
               "TN",
               "TO",
               "TT",
               "TV",
               "TW",
               "TZ",
               "UA",
               "UG",
               "US",
               "UY",
               "UZ",
               "VC",
               "VU",
               "WS",
               "XK",
               "ZA",
               "ZM",
               "ZW"
            ],
            "disc_number":1,
            "duration_ms":258533,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/4I116SyJOoimDfIZBIOiiA"
            },
            "href":"https://api.spotify.com/v1/tracks/4I116SyJOoimDfIZBIOiiA",
            "id":"4I116SyJOoimDfIZBIOiiA",
            "is_local":False,
            "name":"Take Me Under",
            "preview_url":"https://p.scdn.co/mp3-preview/5d0ccc6cf76828018a95b414a4034f2b161495d8?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":11,
            "type":"track",
            "uri":"spotify:track:4I116SyJOoimDfIZBIOiiA"
         },
         {
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
                  },
                  "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
                  "id":"2xiIXseIJcq3nG7C8fHeBj",
                  "name":"Three Days Grace",
                  "type":"artist",
                  "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
               }
            ],
            "available_markets":[
               
            ],
            "disc_number":1,
            "duration_ms":210666,
            "explicit":False,
            "external_urls":{
               "spotify":"https://open.spotify.com/track/2nviKdUcbsHXulMXKqIhDI"
            },
            "href":"https://api.spotify.com/v1/tracks/2nviKdUcbsHXulMXKqIhDI",
            "id":"2nviKdUcbsHXulMXKqIhDI",
            "is_local":False,
            "name":"Overrated",
            "preview_url":"https://p.scdn.co/mp3-preview/4a38f1a4490506d25dad0ae6c626f7da7e5226ab?cid=2f1bc82113914f19a1cc66af6caa2cfc",
            "track_number":12,
            "type":"track",
            "uri":"spotify:track:2nviKdUcbsHXulMXKqIhDI"
         }
      ],
      "limit":50,
      "next":"None",
      "offset":0,
      "previous":"None",
      "total":12
   },
   "type":"album",
   "uri":"spotify:album:13topfW33NjnACjnRiZBX7"
}

spotify_test_artist_lp = {
   "artists":{
      "href":"https://api.spotify.com/v1/search?query=Linkin+Park&type=artist&market=RU&offset=0&limit=10",
      "items":[
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz"
            },
            "followers":{
               "href":"None",
               "total":18832455
            },
            "genres":[
               "alternative metal",
               "nu metal",
               "post-grunge",
               "rap metal"
            ],
            "href":"https://api.spotify.com/v1/artists/6XyY86QOPPrYVGvF9ch6wz",
            "id":"6XyY86QOPPrYVGvF9ch6wz",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/1685533969d5b68cbc630f991e873bd6467f1814",
                  "width":640
               },
               {
                  "height":320,
                  "url":"https://i.scdn.co/image/f759994946aa42851e5293083f472c96c1753105",
                  "width":320
               },
               {
                  "height":160,
                  "url":"https://i.scdn.co/image/0b0925b544b46d90a549f25a7f754ce6e59e6be2",
                  "width":160
               }
            ],
            "name":"Linkin Park",
            "popularity":88,
            "type":"artist",
            "uri":"spotify:artist:6XyY86QOPPrYVGvF9ch6wz"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/7D4sWEhlSOGzN9MfibtSsx"
            },
            "followers":{
               "href":"None",
               "total":3136
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/7D4sWEhlSOGzN9MfibtSsx",
            "id":"7D4sWEhlSOGzN9MfibtSsx",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b2738cec07339dde4484d57f8517",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e028cec07339dde4484d57f8517",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d000048518cec07339dde4484d57f8517",
                  "width":64
               }
            ],
            "name":"The Linkin Park Band",
            "popularity":3,
            "type":"artist",
            "uri":"spotify:artist:7D4sWEhlSOGzN9MfibtSsx"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/54t6hlkGZHlMTC0Ndh0E5A"
            },
            "followers":{
               "href":"None",
               "total":310
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/54t6hlkGZHlMTC0Ndh0E5A",
            "id":"54t6hlkGZHlMTC0Ndh0E5A",
            "images":[

            ],
            "name":"Karaoke - Linkin Park",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:54t6hlkGZHlMTC0Ndh0E5A"
         }
      ],
      "limit":10,
      "next":"None",
      "offset":0,
      "previous":"None",
      "total":3
   }
}

spotify_test_album_meteora = {
   "albums":{
      "href":"https://api.spotify.com/v1/search?query=Meteora&type=album&market=RU&offset=0&limit=10",
      "items":[
         {
            "album_type":"album",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz"
                  },
                  "href":"https://api.spotify.com/v1/artists/6XyY86QOPPrYVGvF9ch6wz",
                  "id":"6XyY86QOPPrYVGvF9ch6wz",
                  "name":"Linkin Park",
                  "type":"artist",
                  "uri":"spotify:artist:6XyY86QOPPrYVGvF9ch6wz"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/4Gfnly5CzMJQqkUFfoHaP3"
            },
            "href":"https://api.spotify.com/v1/albums/4Gfnly5CzMJQqkUFfoHaP3",
            "id":"4Gfnly5CzMJQqkUFfoHaP3",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273b4ad7ebaf4575f120eb3f193",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02b4ad7ebaf4575f120eb3f193",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851b4ad7ebaf4575f120eb3f193",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2003-03-24",
            "release_date_precision":"day",
            "total_tracks":13,
            "type":"album",
            "uri":"spotify:album:4Gfnly5CzMJQqkUFfoHaP3"
         },
         {
            "album_type":"album",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz"
                  },
                  "href":"https://api.spotify.com/v1/artists/6XyY86QOPPrYVGvF9ch6wz",
                  "id":"6XyY86QOPPrYVGvF9ch6wz",
                  "name":"Linkin Park",
                  "type":"artist",
                  "uri":"spotify:artist:6XyY86QOPPrYVGvF9ch6wz"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/0f7R0jf0pcTb6K6IVVPcMD"
            },
            "href":"https://api.spotify.com/v1/albums/0f7R0jf0pcTb6K6IVVPcMD",
            "id":"0f7R0jf0pcTb6K6IVVPcMD",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b27389a8fab8bf8cd2b77da1fd17",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e0289a8fab8bf8cd2b77da1fd17",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d0000485189a8fab8bf8cd2b77da1fd17",
                  "width":64
               }
            ],
            "name":"Meteora (Bonus Edition)",
            "release_date":"2003-03-24",
            "release_date_precision":"day",
            "total_tracks":16,
            "type":"album",
            "uri":"spotify:album:0f7R0jf0pcTb6K6IVVPcMD"
         },
         {
            "album_type":"album",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz"
                  },
                  "href":"https://api.spotify.com/v1/artists/6XyY86QOPPrYVGvF9ch6wz",
                  "id":"6XyY86QOPPrYVGvF9ch6wz",
                  "name":"Linkin Park",
                  "type":"artist",
                  "uri":"spotify:artist:6XyY86QOPPrYVGvF9ch6wz"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/4flcwtqnLoKZJ2wrCp1aJq"
            },
            "href":"https://api.spotify.com/v1/albums/4flcwtqnLoKZJ2wrCp1aJq",
            "id":"4flcwtqnLoKZJ2wrCp1aJq",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273fb7e648af7f3cc7054394d73",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02fb7e648af7f3cc7054394d73",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851fb7e648af7f3cc7054394d73",
                  "width":64
               }
            ],
            "name":"Meteora Live Around the World",
            "release_date":"2012-06-05",
            "release_date_precision":"day",
            "total_tracks":7,
            "type":"album",
            "uri":"spotify:album:4flcwtqnLoKZJ2wrCp1aJq"
         },
         {
            "album_type":"album",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/1yLIaxyVkZnLMXhfRSYEjV"
                  },
                  "href":"https://api.spotify.com/v1/artists/1yLIaxyVkZnLMXhfRSYEjV",
                  "id":"1yLIaxyVkZnLMXhfRSYEjV",
                  "name":"Johannes Bornlöf",
                  "type":"artist",
                  "uri":"spotify:artist:1yLIaxyVkZnLMXhfRSYEjV"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/3PLSbFdaSc9nHiZsdutrAz"
            },
            "href":"https://api.spotify.com/v1/albums/3PLSbFdaSc9nHiZsdutrAz",
            "id":"3PLSbFdaSc9nHiZsdutrAz",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273e94fc5a65c2ad71d82564179",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02e94fc5a65c2ad71d82564179",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851e94fc5a65c2ad71d82564179",
                  "width":64
               }
            ],
            "name":"The Road To Meteora",
            "release_date":"2016-06-09",
            "release_date_precision":"day",
            "total_tracks":7,
            "type":"album",
            "uri":"spotify:album:3PLSbFdaSc9nHiZsdutrAz"
         },
         {
            "album_type":"single",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/4m4ywwSd3EtlfquQLUHnyW"
                  },
                  "href":"https://api.spotify.com/v1/artists/4m4ywwSd3EtlfquQLUHnyW",
                  "id":"4m4ywwSd3EtlfquQLUHnyW",
                  "name":"SSIEGE",
                  "type":"artist",
                  "uri":"spotify:artist:4m4ywwSd3EtlfquQLUHnyW"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/7hZXWxFbOEjKDBJPsModzR"
            },
            "href":"https://api.spotify.com/v1/albums/7hZXWxFbOEjKDBJPsModzR",
            "id":"7hZXWxFbOEjKDBJPsModzR",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273a432158f80c0af3c2e0abfb3",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02a432158f80c0af3c2e0abfb3",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851a432158f80c0af3c2e0abfb3",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2021-04-12",
            "release_date_precision":"day",
            "total_tracks":5,
            "type":"album",
            "uri":"spotify:album:7hZXWxFbOEjKDBJPsModzR"
         },
         {
            "album_type":"single",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2RmEoDzAVo3AKLolGZ1Uss"
                  },
                  "href":"https://api.spotify.com/v1/artists/2RmEoDzAVo3AKLolGZ1Uss",
                  "id":"2RmEoDzAVo3AKLolGZ1Uss",
                  "name":"Spirits Of Our Dreams",
                  "type":"artist",
                  "uri":"spotify:artist:2RmEoDzAVo3AKLolGZ1Uss"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/16Qj1HzFQjQIecbg8TaDtp"
            },
            "href":"https://api.spotify.com/v1/albums/16Qj1HzFQjQIecbg8TaDtp",
            "id":"16Qj1HzFQjQIecbg8TaDtp",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b27341455b9bbce71c61a1343fee",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e0241455b9bbce71c61a1343fee",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d0000485141455b9bbce71c61a1343fee",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2020-04-03",
            "release_date_precision":"day",
            "total_tracks":4,
            "type":"album",
            "uri":"spotify:album:16Qj1HzFQjQIecbg8TaDtp"
         },
         {
            "album_type":"single",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/2Bt2ODA1l9fynTFOm6plxF"
                  },
                  "href":"https://api.spotify.com/v1/artists/2Bt2ODA1l9fynTFOm6plxF",
                  "id":"2Bt2ODA1l9fynTFOm6plxF",
                  "name":"Rentø",
                  "type":"artist",
                  "uri":"spotify:artist:2Bt2ODA1l9fynTFOm6plxF"
               },
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/7sMOGsm8T0YZ230abl9TcP"
                  },
                  "href":"https://api.spotify.com/v1/artists/7sMOGsm8T0YZ230abl9TcP",
                  "id":"7sMOGsm8T0YZ230abl9TcP",
                  "name":"Nōpi",
                  "type":"artist",
                  "uri":"spotify:artist:7sMOGsm8T0YZ230abl9TcP"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/3D6yOwGHaalPh4S6J1rxxX"
            },
            "href":"https://api.spotify.com/v1/albums/3D6yOwGHaalPh4S6J1rxxX",
            "id":"3D6yOwGHaalPh4S6J1rxxX",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b2731097f5a0c6227e8b8f591e8a",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e021097f5a0c6227e8b8f591e8a",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d000048511097f5a0c6227e8b8f591e8a",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2020-09-25",
            "release_date_precision":"day",
            "total_tracks":2,
            "type":"album",
            "uri":"spotify:album:3D6yOwGHaalPh4S6J1rxxX"
         },
         {
            "album_type":"album",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/0t72MIf4UmwUxyOlv4G7i0"
                  },
                  "href":"https://api.spotify.com/v1/artists/0t72MIf4UmwUxyOlv4G7i0",
                  "id":"0t72MIf4UmwUxyOlv4G7i0",
                  "name":"Imy",
                  "type":"artist",
                  "uri":"spotify:artist:0t72MIf4UmwUxyOlv4G7i0"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/5eLKZzDpGiRcKodjx72smn"
            },
            "href":"https://api.spotify.com/v1/albums/5eLKZzDpGiRcKodjx72smn",
            "id":"5eLKZzDpGiRcKodjx72smn",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273dab85c6b84c026f2773ed3f0",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02dab85c6b84c026f2773ed3f0",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851dab85c6b84c026f2773ed3f0",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2019-10-27",
            "release_date_precision":"day",
            "total_tracks":7,
            "type":"album",
            "uri":"spotify:album:5eLKZzDpGiRcKodjx72smn"
         },
         {
            "album_type":"single",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/4FuFFzlzYgn3Yu2rxLhvdN"
                  },
                  "href":"https://api.spotify.com/v1/artists/4FuFFzlzYgn3Yu2rxLhvdN",
                  "id":"4FuFFzlzYgn3Yu2rxLhvdN",
                  "name":"Heatbeat",
                  "type":"artist",
                  "uri":"spotify:artist:4FuFFzlzYgn3Yu2rxLhvdN"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/2ZzePAEy9blKzJQa0ryhpI"
            },
            "href":"https://api.spotify.com/v1/albums/2ZzePAEy9blKzJQa0ryhpI",
            "id":"2ZzePAEy9blKzJQa0ryhpI",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273c2d40e102fcea0bb9682326f",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02c2d40e102fcea0bb9682326f",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851c2d40e102fcea0bb9682326f",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2017-08-04",
            "release_date_precision":"day",
            "total_tracks":1,
            "type":"album",
            "uri":"spotify:album:2ZzePAEy9blKzJQa0ryhpI"
         },
         {
            "album_type":"single",
            "artists":[
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/4BTE0A9MKmuIkzowME4xPr"
                  },
                  "href":"https://api.spotify.com/v1/artists/4BTE0A9MKmuIkzowME4xPr",
                  "id":"4BTE0A9MKmuIkzowME4xPr",
                  "name":"Masi Kohestani",
                  "type":"artist",
                  "uri":"spotify:artist:4BTE0A9MKmuIkzowME4xPr"
               },
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/1D4dzvQBbR36MRnCeBrzy4"
                  },
                  "href":"https://api.spotify.com/v1/artists/1D4dzvQBbR36MRnCeBrzy4",
                  "id":"1D4dzvQBbR36MRnCeBrzy4",
                  "name":"More Than Human",
                  "type":"artist",
                  "uri":"spotify:artist:1D4dzvQBbR36MRnCeBrzy4"
               },
               {
                  "external_urls":{
                     "spotify":"https://open.spotify.com/artist/1Bg2lZo0gm2q7NXh8vJAwK"
                  },
                  "href":"https://api.spotify.com/v1/artists/1Bg2lZo0gm2q7NXh8vJAwK",
                  "id":"1Bg2lZo0gm2q7NXh8vJAwK",
                  "name":"Solarquest",
                  "type":"artist",
                  "uri":"spotify:artist:1Bg2lZo0gm2q7NXh8vJAwK"
               }
            ],
            "external_urls":{
               "spotify":"https://open.spotify.com/album/1MO2Xnk3eR6UIQoRDOzl62"
            },
            "href":"https://api.spotify.com/v1/albums/1MO2Xnk3eR6UIQoRDOzl62",
            "id":"1MO2Xnk3eR6UIQoRDOzl62",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b2734640c783031c55c73194d040",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e024640c783031c55c73194d040",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d000048514640c783031c55c73194d040",
                  "width":64
               }
            ],
            "name":"Meteora",
            "release_date":"2020-12-04",
            "release_date_precision":"day",
            "total_tracks":3,
            "type":"album",
            "uri":"spotify:album:1MO2Xnk3eR6UIQoRDOzl62"
         }
      ],
      "limit":10,
      "next":"https://api.spotify.com/v1/search?query=Meteora&type=album&market=RU&offset=10&limit=10",
      "offset":0,
      "previous":"None",
      "total":137
   }
}

spotify_test_track_json = {
   "album":{
      "album_type":"single",
      "artists":[
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
            },
            "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
            "id":"2xiIXseIJcq3nG7C8fHeBj",
            "name":"Three Days Grace",
            "type":"artist",
            "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
         }
      ],
      "external_urls":{
         "spotify":"https://open.spotify.com/album/6S7lvN6dnZ7EU8TPujw7gd"
      },
      "href":"https://api.spotify.com/v1/albums/6S7lvN6dnZ7EU8TPujw7gd",
      "id":"6S7lvN6dnZ7EU8TPujw7gd",
      "images":[
         {
            "height":640,
            "url":"https://i.scdn.co/image/ab67616d0000b273f84f503fbcacca302785b94a",
            "width":640
         },
         {
            "height":300,
            "url":"https://i.scdn.co/image/ab67616d00001e02f84f503fbcacca302785b94a",
            "width":300
         },
         {
            "height":64,
            "url":"https://i.scdn.co/image/ab67616d00004851f84f503fbcacca302785b94a",
            "width":64
         }
      ],
      "name":"Rolling Stone Original (EP)",
      "release_date":"2003-07-22",
      "release_date_precision":"day",
      "total_tracks":4,
      "type":"album",
      "uri":"spotify:album:6S7lvN6dnZ7EU8TPujw7gd"
   },
   "artists":[
      {
         "external_urls":{
            "spotify":"https://open.spotify.com/artist/2xiIXseIJcq3nG7C8fHeBj"
         },
         "href":"https://api.spotify.com/v1/artists/2xiIXseIJcq3nG7C8fHeBj",
         "id":"2xiIXseIJcq3nG7C8fHeBj",
         "name":"Three Days Grace",
         "type":"artist",
         "uri":"spotify:artist:2xiIXseIJcq3nG7C8fHeBj"
      }
   ],
   "disc_number":1,
   "duration_ms":239680,
   "explicit":False,
   "external_ids":{
      "isrc":"USJI10401012"
   },
   "external_urls":{
      "spotify":"https://open.spotify.com/track/7e2073Iang0hKXlFoffwpF"
   },
   "href":"https://api.spotify.com/v1/tracks/7e2073Iang0hKXlFoffwpF",
   "id":"7e2073Iang0hKXlFoffwpF",
   "is_local":False,
   "is_playable":True,
   "name":"I Hate Everything About You - Live Acoustic - Rolling Stone Original (EP)",
   "popularity":19,
   "preview_url":"https://p.scdn.co/mp3-preview/c598d06980413ca6561d9ebea08bf73e1bb1d710?cid=2f1bc82113914f19a1cc66af6caa2cfc",
   "track_number":4,
   "type":"track",
   "uri":"spotify:track:7e2073Iang0hKXlFoffwpF"
}

spotify_test_album_json = {
   "album_type":"album",
   "artists":[
      {
         "external_urls":{
            "spotify":"https://open.spotify.com/artist/1kDGbuxWknIKx4FlgWxiSp"
         },
         "href":"https://api.spotify.com/v1/artists/1kDGbuxWknIKx4FlgWxiSp",
         "id":"1kDGbuxWknIKx4FlgWxiSp",
         "name":"Nothing But Thieves",
         "type":"artist",
         "uri":"spotify:artist:1kDGbuxWknIKx4FlgWxiSp"
      }
   ],
   "external_urls":{
      "spotify":"https://open.spotify.com/album/5LNmaMITXXVrEm4fnyUbrd"
   },
   "href":"https://api.spotify.com/v1/albums/5LNmaMITXXVrEm4fnyUbrd",
   "id":"5LNmaMITXXVrEm4fnyUbrd",
   "images":[
      {
         "height":640,
         "url":"https://i.scdn.co/image/ab67616d0000b2731cf2d58ddfedf57112d7ef76",
         "width":640
      },
      {
         "height":300,
         "url":"https://i.scdn.co/image/ab67616d00001e021cf2d58ddfedf57112d7ef76",
         "width":300
      },
      {
         "height":64,
         "url":"https://i.scdn.co/image/ab67616d000048511cf2d58ddfedf57112d7ef76",
         "width":64
      }
   ],
   "name":"Moral Panic",
   "release_date":"2020-10-23",
   "release_date_precision":"day",
   "total_tracks":11,
   "type":"album",
   "uri":"spotify:album:5LNmaMITXXVrEm4fnyUbrd"
}

spotify_test_artist_json = {
   "external_urls":{
      "spotify":"https://open.spotify.com/artist/6oFs3qk4VepIVFdoD4jmsy"
   },
   "followers":{
      "href":"None",
      "total":537818
   },
   "genres":[
      "electropop",
      "modern alternative rock",
      "modern rock",
      "pixie",
      "pop",
      "pop emo",
      "pop punk",
      "rock"
   ],
   "href":"https://api.spotify.com/v1/artists/6oFs3qk4VepIVFdoD4jmsy",
   "id":"6oFs3qk4VepIVFdoD4jmsy",
   "images":[
      {
         "height":640,
         "url":"https://i.scdn.co/image/65a9f5630791c716b1b56ac2c69f75cc7843d326",
         "width":640
      },
      {
         "height":320,
         "url":"https://i.scdn.co/image/029965032ce2434040f45a2c0dfdb2605dc8c170",
         "width":320
      },
      {
         "height":160,
         "url":"https://i.scdn.co/image/4b0d80fd2285da6a98edcf897c38159d05d42025",
         "width":160
      }
   ],
   "name":"PVRIS",
   "popularity":67,
   "type":"artist",
   "uri":"spotify:artist:6oFs3qk4VepIVFdoD4jmsy"
}

spotify_search_artists_by_query_json = {
   "artists":{
      "href":"https://api.spotify.com/v1/search?query=PVRIS&type=artist&market=RU&offset=0&limit=10",
      "items":[
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/6oFs3qk4VepIVFdoD4jmsy"
            },
            "followers":{
               "href":"None",
               "total":537818
            },
            "genres":[
               "electropop",
               "modern alternative rock",
               "modern rock",
               "pixie",
               "pop",
               "pop emo",
               "pop punk",
               "rock"
            ],
            "href":"https://api.spotify.com/v1/artists/6oFs3qk4VepIVFdoD4jmsy",
            "id":"6oFs3qk4VepIVFdoD4jmsy",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/65a9f5630791c716b1b56ac2c69f75cc7843d326",
                  "width":640
               },
               {
                  "height":320,
                  "url":"https://i.scdn.co/image/029965032ce2434040f45a2c0dfdb2605dc8c170",
                  "width":320
               },
               {
                  "height":160,
                  "url":"https://i.scdn.co/image/4b0d80fd2285da6a98edcf897c38159d05d42025",
                  "width":160
               }
            ],
            "name":"PVRIS",
            "popularity":67,
            "type":"artist",
            "uri":"spotify:artist:6oFs3qk4VepIVFdoD4jmsy"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/4JMdHrUOSZKdgSeqYNWxB2"
            },
            "followers":{
               "href":"None",
               "total":0
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/4JMdHrUOSZKdgSeqYNWxB2",
            "id":"4JMdHrUOSZKdgSeqYNWxB2",
            "images":[

            ],
            "name":"SANTANA PVRIS",
            "popularity":1,
            "type":"artist",
            "uri":"spotify:artist:4JMdHrUOSZKdgSeqYNWxB2"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/1YgZO4nBPIiXXSy1T3E2LN"
            },
            "followers":{
               "href":"None",
               "total":22
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/1YgZO4nBPIiXXSy1T3E2LN",
            "id":"1YgZO4nBPIiXXSy1T3E2LN",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b273b465a10daca8f0486df66e38",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e02b465a10daca8f0486df66e38",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d00004851b465a10daca8f0486df66e38",
                  "width":64
               }
            ],
            "name":"PVRISWHITE",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:1YgZO4nBPIiXXSy1T3E2LN"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/2AlpUaktyXGg9SsMBjdvhD"
            },
            "followers":{
               "href":"None",
               "total":19
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/2AlpUaktyXGg9SsMBjdvhD",
            "id":"2AlpUaktyXGg9SsMBjdvhD",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ec41a7ea52ee85966dc3a1f390b1aa63e53ea700",
                  "width":640
               },
               {
                  "height":320,
                  "url":"https://i.scdn.co/image/35313acd012c2fa7f02b16f31f8c2163404eb4e4",
                  "width":320
               },
               {
                  "height":160,
                  "url":"https://i.scdn.co/image/581bc021245657ed317653f10d476ad5887f28f4",
                  "width":160
               }
            ],
            "name":"Pvris Chola",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:2AlpUaktyXGg9SsMBjdvhD"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/03A55K30Xqdd3SLxWhsviH"
            },
            "followers":{
               "href":"None",
               "total":3
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/03A55K30Xqdd3SLxWhsviH",
            "id":"03A55K30Xqdd3SLxWhsviH",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/12ef4e7761b38d66dc802fee9b4296fc1625fbe5",
                  "width":640
               },
               {
                  "height":320,
                  "url":"https://i.scdn.co/image/f7e10a07199e6314989f123635b4ac96173d61b4",
                  "width":320
               },
               {
                  "height":160,
                  "url":"https://i.scdn.co/image/024ad1402ad9f696108f674a6afc4bbd8ee1bfe3",
                  "width":160
               }
            ],
            "name":"Pvris Nvpøleøn",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:03A55K30Xqdd3SLxWhsviH"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/4MEHdn8a7BG71gTakkQ8Ae"
            },
            "followers":{
               "href":"None",
               "total":15
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/4MEHdn8a7BG71gTakkQ8Ae",
            "id":"4MEHdn8a7BG71gTakkQ8Ae",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b27370b13210bd543499a95b6705",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e0270b13210bd543499a95b6705",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d0000485170b13210bd543499a95b6705",
                  "width":64
               }
            ],
            "name":"Pvris Jay the God",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:4MEHdn8a7BG71gTakkQ8Ae"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/0MNoPnrAr9MyWdISX73NhW"
            },
            "followers":{
               "href":"None",
               "total":2
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/0MNoPnrAr9MyWdISX73NhW",
            "id":"0MNoPnrAr9MyWdISX73NhW",
            "images":[

            ],
            "name":"Pvris Davinci",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:0MNoPnrAr9MyWdISX73NhW"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/3jK3PCA75ZQIKlvcFSZ28z"
            },
            "followers":{
               "href":"None",
               "total":128
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/3jK3PCA75ZQIKlvcFSZ28z",
            "id":"3jK3PCA75ZQIKlvcFSZ28z",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b27371f146f380d4d144e883a891",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e0271f146f380d4d144e883a891",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d0000485171f146f380d4d144e883a891",
                  "width":64
               }
            ],
            "name":"Pvris DaVinci",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:3jK3PCA75ZQIKlvcFSZ28z"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/0TcDwPRA4XjjKYX8TxOjPG"
            },
            "followers":{
               "href":"None",
               "total":0
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/0TcDwPRA4XjjKYX8TxOjPG",
            "id":"0TcDwPRA4XjjKYX8TxOjPG",
            "images":[

            ],
            "name":"Pvris Chola",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:0TcDwPRA4XjjKYX8TxOjPG"
         },
         {
            "external_urls":{
               "spotify":"https://open.spotify.com/artist/0Ztk7WdD3t7cBKhmQhD1B7"
            },
            "followers":{
               "href":"None",
               "total":1
            },
            "genres":[

            ],
            "href":"https://api.spotify.com/v1/artists/0Ztk7WdD3t7cBKhmQhD1B7",
            "id":"0Ztk7WdD3t7cBKhmQhD1B7",
            "images":[
               {
                  "height":640,
                  "url":"https://i.scdn.co/image/ab67616d0000b27396096e4aba324b9ec850743b",
                  "width":640
               },
               {
                  "height":300,
                  "url":"https://i.scdn.co/image/ab67616d00001e0296096e4aba324b9ec850743b",
                  "width":300
               },
               {
                  "height":64,
                  "url":"https://i.scdn.co/image/ab67616d0000485196096e4aba324b9ec850743b",
                  "width":64
               }
            ],
            "name":"Pvris Nvpoleon",
            "popularity":0,
            "type":"artist",
            "uri":"spotify:artist:0Ztk7WdD3t7cBKhmQhD1B7"
         }
      ],
      "limit":10,
      "next":"None",
      "offset":0,
      "previous":"None",
      "total":10
   }
}