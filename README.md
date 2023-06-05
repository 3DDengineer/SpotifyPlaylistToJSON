# SpotifyPlaylistToJSON
Exports the Track Name, Track ID, Track Length, and Artist of all Songs in a Spotify Playlist to a JSON Document

Installation
Ensure you have Python installed on your system (version 3.6 or later).

Clone or download the project from the GitHub repository: Spotify Playlist Extraction.

Install the required dependencies by running the following command in your terminal:

bash
Copy code
pip install spotipy PySimpleGUI
Usage
Open the terminal or command prompt and navigate to the project directory.

Run the main.py file using the Python interpreter:

bash
Copy code
python main.py
The application window will appear, allowing you to input the necessary information.

Application Window

Provide the required details in the text input fields:

Client ID: Your Spotify API client ID. You can obtain this by creating a Spotify Developer account and registering a new application.
Client Secret: Your Spotify API client secret. It is generated along with the client ID.
Playlist URL: The URL of the Spotify playlist from which you want to extract the song data.
Click the Extract Song Data button to initiate the extraction process.

The program will authenticate with the Spotify API using your client credentials and retrieve the playlist details.

The song data, including the song ID, track name, artist, and duration in minutes, will be extracted and saved in a JSON file.

The JSON file will be named after the playlist, with spaces replaced by underscores and converted to lowercase. It will be saved in the same directory as the program.

The program will display a success message along with the filename where the data is saved.

You can close the application window after the extraction process is complete.

Configuration
The Spotify Playlist Extraction program saves your configuration for future use. The configuration details, including the client ID, client secret, and playlist URL, are stored in the config.ini file. When you reopen the program, it will load the saved configuration automatically. You can modify the configuration values by updating the corresponding fields in the application window.

Dependencies
The Spotify Playlist Extraction program relies on the following dependencies:

spotipy: A lightweight Python library for the Spotify Web API.
PySimpleGUI: A Python GUI framework for creating simple and easy-to-use interfaces.
These dependencies are automatically installed when you run the pip install command mentioned in the Installation section.

License
This project is licensed under the GNU something somehting i can't remeber licesne idc what you do with it ybh

Contributing
do whatever you want idc

Credits
This was almost entirely written by ChatGPT, i only made a few minor tweaks to get it working smoothly

Contact
Please do not contact me, i don't care.
