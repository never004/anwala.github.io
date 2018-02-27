from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy
import time

ckey = 	'consumer key'
csecret = 'consumer secret'
atoken = 'access token'
asecret = 'access secret'
handle = 'your chosen handle'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

#fin = open('followers.txt', 'r')
fout = open('followercount.txt', 'w')

if(api.verify_credentials):
    print ('Logged in')
for user in tweepy.Cursor(api.followers, screen_name=handle).items():
    try:
        print (user.screen_name, ", ", user.followers_count)
    except TweepError:
        pass
#fin.close()
fout.close()
