# Created by Jesse Son @ youtube.com/c/undrgroundSeoul @ github.com/json469
# Downloading SoundCloud contents must be approved by the owner first!

import soundcloud
import urllib
import os
import requests
import tkinter

# INITIALIZE
CLIENT_ID = 'LvWovRaJZlWCHql0bISuum8Bd2KX79mb'  # Client ID generation is suspended at Soundcloud, therefore using public client ID utilised by yotube-dl python.
client = soundcloud.Client(client_id=CLIENT_ID)

def run(url):

    TRACK_URL = url

    # TRACK IDENTIFY
    track = client.get('/resolve', url=TRACK_URL)
    track_id = track.id
    artist = track.user["username"].replace('/', '@')   # Replacing char / with @, as it disrupts download location eitherwise.
    title = track.title.replace('/', '@')
    title_asciifriendly = url[url.rfind('/')+1:]    # This is the english title used for SoundCloud link useful for naming the audio file as sometimes title is korean.

    print(title_asciifriendly)

    track_standardformat = artist + ' - ' + title
    rootpath = os.path.dirname(os.path.realpath(__file__)) + '\\downloads\\' + track_standardformat
    
    print('Root path: ' + rootpath)
    print ('Identified: ' + track_standardformat)

    # Create parent directory, as most likely this will indiciate whether the image already exists or not.
    if not os.path.exists(rootpath):

        # Try creating directory, as track_standardformat string may contain special characters which prevents windows from creating the folder.
        try:
            os.makedirs(rootpath)
        except Exception as e:
            print ('FILE PATH ERROR: ' + str(e))

        # IMAGE DOWNLOAD
        image_url = (track.artwork_url).replace('-large', '-t500x500')
        image_dlpath = rootpath + '\\' + title_asciifriendly + '.jpg'
        
        try:
            urllib.request.urlretrieve(image_url, image_dlpath)
        except Exception as e:
            print ('IMAGE DOWNLOAD ERROR: ' + str(e))

        print ('Image downloaded successfully.')

        # TRACK DOWNLOAD
        stream_url = 'http://api.soundcloud.com/tracks/%s/stream?client_id=%s' % (track_id, CLIENT_ID)
        audio_dlpath = rootpath + '\\' + title_asciifriendly +'.mp3'

        try:
            urllib.request.urlretrieve(stream_url, audio_dlpath)
        except Exception as e:
            print ('AUDIO DOWNLOAD ERROR: ' + str(e))
        
        print ('Audio downloaded successfully.')

    else:
        print ('ERROR: Terminated because a directory already exists.')

while (True):
    print ('\n\n\n---UNDRGRND SEOUL SOUNDCLOUD DOWNLOADER---')
    url = input('Enter URL: ')
    run(url)

