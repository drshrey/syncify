class Syncify(object):
	def __init__(self, track_name, service, auth=None):
		self.track_name = track_name
		self.found = False
		self.service = service 

	'''Return the track name of this node
	'''
	def get_track_name():
		return self.track_name
	
	'''Return whether this node has been found in Spotify. 
	'''
	def is_found():
		return self.found

	'''Sets true or false to whether the 
	   node's track has been found inside Spotify

	'''
	def set_found(yes_or_no):
		self.found = yes_or_no
	
	'''Sets the track name for the node. 
	'''
	def set_track_name(track_name):
		self.track_name = track_name
