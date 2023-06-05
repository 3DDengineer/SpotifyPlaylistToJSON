import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import PySimpleGUI as sg
import configparser

# Read the configuration from the file
config = configparser.ConfigParser()
config.read('config.ini')

client_id = config.get('Settings', 'client_id', fallback='')
client_secret = config.get('Settings', 'client_secret', fallback='')
playlist_url = config.get('Settings', 'playlist_url', fallback='')

def extract_song_data():
    # Authenticate and create Spotify API client
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Get playlist details
    playlist = sp.playlist(playlist_url)
    playlist_name = playlist['name']
    playlist_tracks = playlist['tracks']['items']

    # Extract song details
    song_data = []
    for track in playlist_tracks:
        song_id = track['track']['id']
        track_name = track['track']['name']
        artist = track['track']['artists'][0]['name']
        duration = track['track']['duration_ms']
        duration_minutes = round(duration / 60000, 2)  # Convert milliseconds to minutes
        song_data.append({'song_id': song_id, 'track_name': track_name, 'artist': artist, 'duration_minutes': duration_minutes})

    # Save data in JSON format with playlist name
    filename = f"{playlist_name.replace(' ', '_').lower()}_data.json"
    with open(filename, 'w') as file:
        json.dump(song_data, file, indent=4)

    print(f"Song IDs and track details extracted and saved successfully in {filename}!")

# Create the layout for the GUI
layout = [
    [sg.Text('Client ID:'), sg.InputText(default_text=client_id, key='-CLIENT_ID-')],
    [sg.Text('Client Secret:'), sg.InputText(default_text=client_secret, key='-CLIENT_SECRET-')],
    [sg.Text('Playlist URL:'), sg.InputText(default_text=playlist_url, key='-PLAYLIST_URL-')],
    [sg.Button('Extract Playlist Data')]
]

# Create the window and display it
window = sg.Window('Spotify Playlist Extraction', layout)

# Event loop to process user input
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Extract Playlist Data':
        client_id = values['-CLIENT_ID-']
        client_secret = values['-CLIENT_SECRET-']
        playlist_url = values['-PLAYLIST_URL-']

        # Save the configuration to the file
        config['Settings'] = {
            'client_id': client_id,
            'client_secret': client_secret,
            'playlist_url': playlist_url
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        extract_song_data()
        break

window.close()
