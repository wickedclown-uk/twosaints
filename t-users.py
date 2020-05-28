#!/usr/bin/python

from collections import Counter
from twython import Twython

APP_KEY = 'YOUR_APP_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

out =[]


target = raw_input("Please enter your target tweeter account: ")
UT = twitter.get_user_timeline(screen_name=target, count=200,include_rts=False)

def search():
	global a
        global id
	for tweet in UT:
                txt = tweet['text']
                for user in txt.split():
                        if user[0] == '@':
                                out.append(user)
                                a = dict(Counter(out))
				id = tweet['id']


for i in range (0,16):
        UT = twitter.get_user_timeline(screen_name=target, count=200,include_rts=False,max_id=id)
	search()

for key, value in sorted (a.iteritems(), key=lambda(k,v): (v,k)):
	print key, value



