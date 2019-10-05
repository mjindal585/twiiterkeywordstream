from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# consumer key, consumer secret, access token, access secret.
ckey = "XXXXX"
csecret = "XXXXXXXXXXXXX"
atoken = "XXXXXXXXXXXXXXXXXX"
asecret = "XXXXXXXXXXXXX"

class StdOutListener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        out = open('out1.txt', 'a', encoding="utf-8")
        out.write(tweet)
        out.write('\n')
        out.close()
        print (username+ " :: "+ tweet)
        return True


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
keywords = ["hello twitter"]
twitterStream = Stream(auth, StdOutListener())
twitterStream.filter(track=keywords, languages=["en"])
