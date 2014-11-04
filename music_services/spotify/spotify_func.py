import spotify
import threading
#Spotify Library Functions

#Adds a track to the appropriate music service playlist
#Returns a boolean for validity
#def adds_to_playlist(syncifyObject, spotifyClient)

#Function that helps login_correctly 
#Function that properly logins without failure when authentication details are True
def login_correctly(user,password):
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
	session.login(user, password)
	logged_in_event.wait()
	return session

#Search through songs in each playlist of Spotify
#Returns a boolean --> False if doesn't exist; True if does exist 
def search(syncifyObject, spotifyClient):
	playlist = ''
	for tmp_list in spotifyClient.playlist_container:
		if(tmp_list.load().name == syncifyObject.serviceinfo.service_name):
			playlist = tmp_list
			break
	if(playlist == ''):
		print "Could not find appropriate music service playlist"
		return False
	try:
		for track in playlist.tracks:
			print track.load().name
			if track.load().name == syncifyObject.trackinfo.name:
				return True
		return False
	except AttributeError:
		print "Weird unicode object but it seems like we got the right playlist so I'll return True for now. search function."
		return True

#Create a music service playlist
#Returns a boolean for validity
def create_playlist(syncifyObject, spotifyClient):
	try:
		container = spotifyClient.playlist_container; 
		playlist_name = syncifyObject.serviceinfo.service_name
		playlist = container.add_new_playlist(playlist_name)
		print "New playlist was created: ", playlist_name
		return playlist
	except spotify.LibError:
		print "LibError, we couldn't create a new service playlist. create_playlist."
		return None

#Returns the appropriate track object of the track name and artist
def get_track(name, artist, spotifyClient):
	try:
		track = None
		query = "title:"+name+" artist:'"+artist+"'"
		results = spotifyClient.search(query).load()
		track = results.tracks[0]	
		if track == None:
			print "Could not get track URI"
		return track
	except spotify.error.Timeout:
		print "Spotify was not able to search for", track

#Add given track to given playlist name
def add_to_playlist(track, playlist):
	try:
		playlist.add_tracks(track)
		return True
	except(spotify.LibError, TypeError, AttributeError):
		if(TypeError):
			print "The playlist object is not valid"
			return False
		if(AttributeError):
			print "The track object is null"
			return False
		print "Unicode object. Maybe the Track object is corrupted or not valid?"
		return False



