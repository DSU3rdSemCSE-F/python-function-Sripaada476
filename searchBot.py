import tweepy
import time

consumer_key = 'kmgLbvjxSEApA4h2Mow8GEJld'
consumer_secret = '33ZfLj5rWPgA4evhxdGHQMjynTjl6NUZYCJ6pFzijs17T2b5lt'

key = '926247580199030784-tTlCGRNCVStO1GYd23IcY8zMdP1efo9'
secret = 'OriTu8Gk3f81XpTXw2WbRMOz4Y6p1gsBniAJPssmO2mz8'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

hashtag = "#gaming" or "#gamers"
tweetNumber = 10

tweets = tweepy.Cursor(api.search,hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()            
