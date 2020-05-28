#!/usr/bin/python
# search
from twython import Twython

APP_KEY = 'YOUR_APP_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


target = raw_input("Please enter your target tweeter account: ")
search = raw_input("What word do you want to search for? :")

UT = twitter.get_user_timeline(screen_name=target, count=1,include_rts=False)

for i in range (0,16):
	UT = twitter.get_user_timeline(screen_name=target, count=200,include_rts=False,max_id=id)
	for tweet in UT:
		txt = tweet['text']
		date = tweet['created_at']
		for line in txt.splitlines():
			if search in line:
				print date+' '+line
		id = tweet['id']
