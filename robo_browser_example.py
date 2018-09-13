import re
from robobrowser import RoboBrowser

# Browse to Genius
browser = RoboBrowser(history=True)
browser.open('http://genius.com/')

# Search for Porcupine Tree
form = browser.get_form(action='/search')
form                # <RoboForm q=>
form['q'].value = 'porcupine tree'
browser.submit_form(form)

# Look up the first song
songs = browser.select('.song_link')
browser.follow_link(songs[0])
lyrics = browser.select('.lyrics')
lyrics[0].text      # \nHear the sound of music ...

# Back to results page
browser.back()

# Look up my favorite song
song_link = browser.get_link('trains')
browser.follow_link(song_link)

# Can also search HTML using regex patterns
lyrics = browser.find(class_=re.compile(r'\blyrics\b'))
lyrics.text         # \nTrain set and match spied under the blind...