#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import sys
import requests
from urllib.parse import urlparse

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = 	'MpAzsutpq70RBH7jS84jmFE4K'
csecret = 'KaHIDsjrZjSYbK3ZwqWOHtJwlAg2jsJDTRW9PTPR6RXlWqXm9A'
atoken = '957261812457725952-EZevzr6lZWrT9tTUf2iPbJKc6sIhbyf'
asecret = 'A59ee3RAj2RjQSQYyJaGuTcpg6XhaLRQJhXJdZwnpEEGG'

class listener(StreamListener):
    totalLinks = 0

    def on_data(self, data):
        #learn about tweet json structure: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
        tweetJson = json.loads(data)
        if ( len(tweetJson) != 0 ):
            if( 'user' in tweetJson ):
                #access tweet here
                tweetJson['user']
            else:
                print('user' not in tweetJson)
        else:
            print('tweetJson is empty')
        #tweet = tweetJson['text']
        username = tweetJson['user']['screen_name']
        links = tweetJson['entities']['urls']
        if( len(links) != 0 and tweetJson['truncated'] == False ):
            listener.totalLinks += 1
            links = self.getLinksFromTweet(links)
            print( username )
            for l in links:
                o = urlparse(l)
                r = requests.head(l, allow_redirects=True)
                if not (o.netloc == 'twitter.com'): #omit links from twitter domain (twitter.com)
                    print (r.status_code)
                    print('\t', l)
                    with open("listlinks.txt","a") as myFile:
                        myFile.write(l + '\n')
            print ()
            if (listener.totalLinks > 2000):
                return False
        #print('...sleep for 5 seconds')
        #time.sleep(5)
        return True
    
    def getLinksFromTweet(self, linksDict):
        links = []
        for uri in linksDict:
            links.append( uri['expanded_url'])
        return links

    def on_error(self, status):
        print( status )
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        return True

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
try:
    twitterStream.filter(track=['football'])
except BaseException as e:
    print("Error on_data: %s" % str(e))
