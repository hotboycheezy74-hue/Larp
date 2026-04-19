import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

auth_manager = SpotifyClientCredentials(
    client_id="8fc3b4a3baf54d20b9964ff6cb8021fa",
    client_secret="1745b34295d1441891081fb25a471ecc"
)

sp = spotipy.Spotify(auth_manager=auth_manager)

def search_artist_catalogue(inputdata):
    results = sp.search(q=inputdata['Music']['Artist'], type=["track"], limit=10)
    for track in results["tracks"]["items"]:
        print(track["name"], "-", track["artists"][0]["name"])


def search_general_song(inputdata):
    results = sp.search(q=(inputdata['Music']['Genre'] + inputdata['Music']['Era'] + inputdata['Music']['Era'] + (inputdata['Photo Vibe'] or inputdata['Music']['Energy'])), type=["track"], limit=10)
    for track in results["tracks"]["items"]:
        print(track["name"], "-", track["artists"][0]["name"])
