import sys
#syncify dir includes syncify_object, spotify_func
sys.path.append('/Users/drshrey/python/command_line/syncify/')

import spotify 
import spotify_func 
import syncify_object
import threading

#LOGIN INFORMATION
'''
login_file = open('spotify_login.txt','r')
user = login_file.readline()
print user
password = login_file.readline()
print password
if(user == '' or password == ''):
	print "Enter your login information. Don't worry, you'll only need to do this once"
	user = raw_input("Enter your username: \n")
	password = raw_input("Enter your password : \n")
	login_file = open('spotify_login.txt', 'w')
	login_file.write(user+'\n')
	login_file.write(password+'\n')

'''
#LOGGING IN
session = spotify_func.login_correctly(user, password)
#ADD/SYNC 
testSyncObj = syncify_object.Syncify("Gravity", "Continuum", "John Mayer", "HypeM")

new_track = None
valid_playlist = spotify_func.search_playlist(testSyncObj, session)

#Check if valid_playlist is empty
#If valid_playlist is None, create new playlist and add track
if valid_playlist == None:
	valid_playlist = spotify_func.create_playlist(testSyncObj, session)
	new_track = spotify_func.get_track(testSyncObj.trackinfo.name, testSyncObj.trackinfo.artist, session)	
	valid_add = spotify_func.add_to_playlist(new_track, valid_playlist)


valid_track = spotify_func.search_track(valid_playlist, testSyncObj, session)

#Check if track is found inside valid_playlist
#If track is inside valid_playlist, ignore and just print done
if valid_track == False:
	print "Track is not inside playlist, so adding to it."
	new_track = spotify_func.get_track(testSyncObj.trackinfo.name, testSyncObj.trackinfo.artist,session)
	valid_add = spotify_func.add_to_playlist(new_track, valid_playlist)

print "Done with syncing!"
