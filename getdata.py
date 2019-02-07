import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Using Client Credentials for authorization
client_credentials_manager = SpotifyClientCredentials(client_id="f2d11bfce2cf4bae8e096454ca4299ed",client_secret="0192b251aff04567a49d33d83287a254")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# get access token for spotify
token = client_credentials_manager.get_access_token()
