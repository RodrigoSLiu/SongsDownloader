import spotipy
import urllib.parse
import urllib.request
import re
from pytube import YouTube
from spotipy.oauth2 import SpotifyClientCredentials

path = input("Enter the path of your file: ") #C:\Users\---\Desktop\
uri = input("Enter the Spotify playlist uri: ") #spotify:playlist:4FroAeQwZrJCYYyJroHd9V
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='', client_secret=''))

songs = spotify.playlist_items(uri)
tracks = []

for i, playlist in enumerate(songs['items']):
    # [[Songs0, Artist0], [Songs1, Artist1]]
    tracks.append([songs['items'][i]['track']['name'], songs['items'][i]['track']['artists'][0]['name']])

for song in tracks:
    songToSearch = ' '.join([song[0], song[1]])
    query = urllib.parse.quote(songToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    html = urllib.request.urlopen(url)
    video_links = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    YouTube('https://www.youtube.com/watch?v=' + video_links[0]).streams.first().download(path)
