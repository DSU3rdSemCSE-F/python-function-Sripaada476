import tweepy
import time

consumer_key = 'kmgLbvjxSEApA4h2Mow8GEJld'
consumer_secret = '33ZfLj5rWPgA4evhxdGHQMjynTjl6NUZYCJ6pFzijs17T2b5lt'

key = '926247580199030784-tTlCGRNCVStO1GYd23IcY8zMdP1efo9'
secret = 'OriTu8Gk3f81XpTXw2WbRMOz4Y6p1gsBniAJPssmO2mz8'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#ultimatebot' or 'python' or '#hey' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "sure pls dm me",tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)

while True:
    reply()
    time.sleep(15)
