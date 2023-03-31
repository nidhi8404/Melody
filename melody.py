from asyncio import exceptions
from distutils import core
import tkinter as tk
import spotipy
import webbrowser
import pyautogui as pg
import time
import json

clientID = '39c53e21574647f29114e241ccaa7aa4'
clientSecret = 'cfba8de7092247bea37b271672be45de'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)

class MusicPlayerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        # Create a label to display the user's display name
        user_name = spotifyObject.current_user()['display_name']
        self.user_label = tk.Label(master, text="Welcome, " + user_name)
        self.user_label.pack()

        # Create a text box for the user to enter a song name
        self.search_box_label = tk.Label(master, text="Enter a song name:")
        self.search_box_label.pack()
        self.search_box = tk.Entry(master)
        self.search_box.pack()

        # Create a button to search for the song
        self.search_button = tk.Button(master, text="Search", command=self.search_song)
        self.search_button.pack()

        # Create a button to exit the program
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

    def search_song(self):
        # Get the user's input from the search box
        search_song = self.search_box.get()

        # Use the Spotify API to search for the song
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']

        if len(song_items) > 0:
            # Get the URL of the first song in the search results
            song_url = song_items[0]['external_urls']['spotify']

            # Open the song in the user's web browser
            webbrowser.open(song_url)

            # Wait for the browser to load the page
            time.sleep(7)

            # Simulate a mouse click to play the song
            pg.click(311,510)
        else:
            # Display an error message if the song is not found
            tk.messagebox.showerror("Error", "Song not found")

root = tk.Tk()
my_gui = MusicPlayerGUI(root)
root.mainloop()
