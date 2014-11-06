Syncify
=====
People use a ton of music applications. Atleast I do., and I find it really annoying whenever I like a song on 8tracks, SoundCloud, HypeM, etc, have to search for it in Spotify, and then finally put it in the Spotify playlist. Ain't nobody got time for that, so I decided to make this. Syncify.

To run, just clone the repo, and put in this command:

```
python syncify.py 
```

It'll ask for your username, and then get the appropriate permissions from you, which you just have to respond 'yes' and 'yes' for. 

Example:
```
$ python syncify.py

Which services do you want to sync? Enter in which numbers are appropriate. If all, then type 'all'.
1 8tracks
2 SoundCloud
3 Hype Machine

$ 8tracks

Do you grant us permission and look through your information on 8tracks, in order to grab your tracks? Type [Y/N]

$ Y

Syncing....

Done! Check out your updated playlists at :
8tracks Finds
Chill Music
```

##To Do:

Spotify Functionality:
Create playlists that don't exist yet [Check] 
Add tracks into playlists that are extracted from Syncify objects [Check]

8tracks Functionality:
Create Syncify objects
Pass to database

MongoDB Functionality:
Set up database to save syncify objects and pass them through to spotify

