import spotipy
import os
import spotipy.util as util
import sys
import argparse 

#GLOBAL VARIABLE FOR SPOTIFY OBJECT
sp = spotipy.Spotify()


#Wrapper to call function easier
def get_token(USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI):
	return util.prompt_for_user_token(USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

#returns a user's playlists (need to be authenticated via oauth)
def user_playlists(token, username):
	product = []
	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlists(username)
		for playlist in playlists['items']:
			product.extend(playlist['name'])
	else:
		print "Can't get token for", username

def search_artist(artist):
	results = []
	artist_name = ' '.join(artist)
	results = sp.search(q=artist_name, limit=20)
	for i,t in enumerate(results['tracks']['items']):
		results[i] = t
	return results


#search for a song	
def search_song(song_uri):
	track = sp.tracks(song_uri)
	return track

#search for duplicate 
def is_duplicate():
	print "Ain't happening"

def get_largest_view():
	print "Ain't happening"

if __name__ == "__main__":
	USERNAME = "drshrey"
	SCOPE = "playlist-read-private"
	CLIENT_ID = "c53692c7a6784abb9867ec41ac72ef09"
	CLIENT_SECRET = "4211d6d236f04950917af55c02c70840"
	REDIRECT_URI="https://google.com"

	#Create spotipy object
	token = get_token(USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
	artist = sys.argv[1:]
	name = sys.argv[len(artist):]
	results = search_artist(artist)
	for key, value in results.iteritems():
		print "KEY1 ", key
		for key2, value2 in value.iteritems():
			print "KEY: ", key2, "\t VALUE: ", value2
