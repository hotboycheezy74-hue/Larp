import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import openai_Module

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

auth_manager = SpotifyClientCredentials(
    client_id="8fc3b4a3baf54d20b9964ff6cb8021fa",
    client_secret="1745b34295d1441891081fb25a471ecc"
)

sp = spotipy.Spotify(auth_manager=auth_manager)

def search_artist_catalogue(inputdata):
    results = sp.search(q=inputdata['Music']['Artist'], type=["track"], limit=10)
    #for track in results["tracks"]["items"]:
        #print(track["name"], "-", track["artists"][0]["name"])

    promptstring = f"Here is a list of 10 songs from a specific artist, give three songs from this list that most accurately fits these key words: {inputdata['Music']['Energy']}, {inputdata['Photo Vibe'] or inputdata['Vibe']}, {results}, and only output the list, no other words"
    return openai_Module.ai_request(promptstring, False).output_text

def search_general_song(inputdata):
    results = sp.search(q=(inputdata['Music']['Genre'] + inputdata['Music']['Era']), type=["track"], limit=10)
    #for track in results["tracks"]["items"]:
        #print(track["name"], "-", track["artists"][0]["name"])

    promptstring = f"Here is a list of 10 songs, give three songs from this list that most accurately fits these key words: {inputdata['Music']['Energy']}, {inputdata['Photo Vibe'] or inputdata['Vibe']}, {results}, and only output the list, no other words"
    return openai_Module.ai_request(promptstring, False).output_text
