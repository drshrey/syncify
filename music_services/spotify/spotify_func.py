import spotipy

'''
This file contains functions that interact with Spotify's API 
'''

#Reading from Credentials file
credentials = fopen("credentials.txt", "r")

#GLOBAL VARIABLES FOR CREDENTIALS
USERNAME = "drshrey"
SCOPE = "-"
CLIENT_ID = credentials.readline()
CLIENT_SECRET = credentials.readline()
REDIRECT_URI = credetials.readline()

#GLOBAL VARIABLE FOR SPOTIFY OBJECT
SP = spotipy.Spotify()

#Idea for efficiency in storing songs list: Trie/ Tree structure of some sort?
#Functions for Spotify
'''Adds track to appropriate track
'''
def add_to_playlist(track)

'''Search for song in Spotify search
'''
def search_song()

'''Create a new playlist with appropriate title if necessary e.g. When a new 8tracks playlist is liked
'''
def create_playlist()
