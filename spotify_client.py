import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

auth_manager = SpotifyClientCredentials(
    client_id="8fc3b4a3baf54d20b9964ff6cb8021fa",
    client_secret="1745b34295d1441891081fb25a471ecc"
)

sp = spotipy.Spotify(auth_manager=auth_manager)

def spotifyTest():
    results = sp.search(q="rnb", type="track", limit=5)

    for track in results["tracks"]["items"]:
        print(track["name"], "-", track["artists"][0]["name"])



def make_query(keyword, artist=None):
    if artist is None or artist == "":
        return keyword
    else:
        return "artist:" + artist + " " + keyword

def search_songs(keyword, artist=None):
    query = make_query(keyword, artist)

    results = sp.search(q=query, type="track", limit=3)

    songs = []
    for track in results["tracks"]["items"]:
        songs.append({
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"]
        })

    return songs

def display_songs(songs):
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['name']} - {song['artist']}")



keyword = "chill"
artist = "SZA"   # or None

songs = search_songs(keyword, artist)

display_songs(songs)

