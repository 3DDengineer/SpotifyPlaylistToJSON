# SpotifyPlaylistToJSON
Exports the Track Name, Track ID, Track Length, and Artist of all Songs in a Spotify Playlist to a JSON Document

## Installation

1. Ensure you have Python installed on your system (version 3.6 or later).
2. Clone or download the project from the GitHub repository https://github.com/3DDengineer/SpotifyPlaylistToJSON
3. Install the required dependencies by running the following command in your terminal:

```bash
pip install spotipy PySimpleGUI json configparser
```
## Usage
1. Open the terminal or command prompt and navigate to the project directory.
2. Run the main.py file using the Python interpreter:

```bash
python main.py
```

3. The application window will appear, allowing you to input the necessary information.

![image](https://github.com/3DDengineer/SpotifyPlaylistToJSON/assets/80202484/87d28095-e1b0-43a2-b100-2e42f8bb785e)

4. Provide the required details in the text input fields:
     1. Client ID: Your Spotify API client ID. You can obtain this by creating a Spotify Developer account and registering a new application. DO NOT SHARE THIS WITH ANYONE
     2. Client Secret: Your Spotify API client secret. It is generated along with the client ID. DO NOT SHARE THIS WITH ANYONE
     3.  Playlist URL: The URL of the Spotify playlist from which you want to extract the song data.

5. Click the Extract Song Data button to initiate the extraction process.

6. The program will authenticate with the Spotify API using your client credentials and retrieve the playlist details.

7. The song data, including the song ID, track name, artist, and duration in minutes, will be extracted and saved in a JSON file.

8. The JSON file will be named after the playlist, with spaces replaced by underscores and converted to lowercase. It will be saved in the same directory as the program.

9. The program will display a success message along with the filename where the data is saved.

10. You can close the application window after the extraction process is complete, but it should happen automatically.


## License
This project is licensed under the GNU something somehting i can't remember licesne idc what you do with it tbh

## Contributing
do whatever you want idc

## Credits
This was almost entirely written by ChatGPT, i only made a few minor tweaks to get it working smoothly

## Contact
Please do not contact me, i don't care.
