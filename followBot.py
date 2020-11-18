import tweepy
import time

consumer_key = 'kmgLbvjxSEApA4h2Mow8GEJld'
consumer_secret = '33ZfLj5rWPgA4evhxdGHQMjynTjl6NUZYCJ6pFzijs17T2b5lt'

key = '926247580199030784-tTlCGRNCVStO1GYd23IcY8zMdP1efo9'
secret = 'OriTu8Gk3f81XpTXw2WbRMOz4Y6p1gsBniAJPssmO2mz8'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def follow_followers(api):
    print("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            print(f"Following {follower.name}")
            follower.follow()

while True:
        follow_followers(api)
        print("Waiting...")
        time.sleep(60)
        