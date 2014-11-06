import sys
#syncify dir includes syncify_object, spotify_func
sys.path.append('/Users/drshrey/python/command_line/syncify/')

import spotify 
import spotify_func 
import syncify_object
import threading

#LOGIN INFORMATION
login_file = open('spotify_login.txt','r')
user = login_file.readline()
password = login_file.readline()
#if(user == '' or password == ''):
print "Enter your login information. Don't worry, you'll only need to do this once"
user = raw_input("Enter your username: \n")
password = raw_input("Enter your password : \n")
login_file = open('spotify_login.txt', 'w')
login_file.write(user+'\n')
login_file.write(password+'\n')

#LOGGING IN
session = spotify_func.login_correctly("drshrey", "Idaman2014")
#ADD/SYNC 
testSyncObj = syncify_object.Syncify("Why Georgia", "Room for Squares", "John Mayer", "8tracks")

new_playlist = None
new_track = None

valid_playlist = spotify_func.search_playlist(testSyncObj, session)
if valid_playlist == False:
	new_playlist = spotify_func.create_playlist(testSyncObj, session)
	new_track = spotify_func.get_track(testSyncObj.trackinfo.name, testSyncobj.trackinfo.artist, session)	
	valid_add = spotify_func.add_to_playlist(new_track, new_playlist)

valid_track = search_track(valid_playlist, testSyncObj, )

