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
#session = spotify_func.login_correctly(user, password)
logged_in_event = threading.Event()
def connection_state_listener(session):
	if session.connection.state is spotify.ConnectionState.LOGGED_IN:
		logged_in_event.set()

session = spotify.Session()
loop = spotify.EventLoop(session)
loop.start()
session.on(
		spotify.SessionEvent.CONNECTION_STATE_UPDATED,
		connection_state_listener
		)
session.login('drshrey', 'Idaman2014')
logged_in_event.wait()
#ADD/SYNC 
testSyncObj = syncify_object.Syncify("Why Georgia", "Room for Squares", "John Mayer", "8tracks")

valid = spotify_func.search(testSyncObj, session)
if(valid == False):
	playlist = spotify_func.create_playlist(testSyncObj, session)
	track = spotify_func.get_track(testSyncObj.trackinfo.name, testSyncObj.trackinfo.artist, session)
	add_valid = spotify_func.add_to_playlist(track, playlist)
	print add_valid

print "HOOKAY"
valid = spotify_func.search(testSyncObj, session)

if(valid == False):
	print "You fucked up somehow"
