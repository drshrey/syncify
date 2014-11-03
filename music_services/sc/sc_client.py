import soundcloud
from sc_func import get_description
credentials = open("sc_credentials.txt", "r")

CLIENT_ID = credentials.readline() 
CLIENT_SECRET = credentials.readline() 
REDIRECT_URI = credentials.readline()

client = soundcloud.Client(
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		redirect_uri=REDIRECT_URI
	)


if __name__ == "__main__":
	print get_description(client)
