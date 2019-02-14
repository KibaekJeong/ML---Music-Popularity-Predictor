import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Using Client Credentials for authorization
client_credentials_manager = SpotifyClientCredentials(client_id="f2d11bfce2cf4bae8e096454ca4299ed",client_secret="0192b251aff04567a49d33d83287a254")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# get access token for spotify
token = client_credentials_manager.get_access_token()
tracks = ["spotify:track:7BKLCZ1jbUBVqRi2FVlTVw"]
track = "7BKLCZ1jbUBVqRi2FVlTVw"
track_info = sp.tracks(tracks)
track_info1 = track_info['tracks'][0]

artist_uri = (track_info1['artists'][0]['uri'])
artist_name = (track_info1['artists'][0]['name'])
song_popularity = (track_info1['popularity'])

artist = sp.artist(artist_uri)
artist_popularity = artist['popularity']
artist_followers =(artist['followers']['total'])

audio_analysis = sp.audio_analysis(track)

print(song_popularity)
print(artist_popularity)
print(audio_analysis['sections'])
print(audio_analysis['segments'])
