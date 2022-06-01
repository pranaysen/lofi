import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


finalList = []

def main():
    credentials = json.load(open("secret.json"))
    client_id = credentials["client_id"]
    client_secret = credentials["client_secret"]

    playlist_idx = 0
    uri = "https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn?si=5dd129e4b18043b5"

    credit_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credit_manager)
    while(playlist_idx != 1000):
        results = sp.user_playlist_tracks("Spotify", uri, offset=playlist_idx)
        extractData(results)
        playlist_idx += 100
    print(len(finalList))


def extractData(tracks):
    for track in tracks["items"]:
        image_url = track['track']['album']['images'][0]['url']
        track_name = track['track']['name']
        finalList.append(track['track']['name'])


if __name__ == "__main__":
    main()