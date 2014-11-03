class Syncify(object):
	def __init__(self, track_name, album, artist, service):
		self.trackinfo = TrackInfo(name=track_name,artist=artist,album=album)
		self.serviceinfo = Service(service_name=service)

class TrackInfo(object):
	def __init__(self, name, artist, album):
		self.name = name
		self.artist = artist
		self.album = album

class Service(object):
	def __init__(self, service_name):
		self.service_name = service_name


