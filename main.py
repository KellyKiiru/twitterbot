import tweepy

all_keys = open("env", "r").read().splitlines()

API_KEY=all_keys[0]
API_KEY_SECRET=all_keys[1]
ACCESS_TOKEN=all_keys[2]
ACCESS_TOKEN_SECRET=all_keys[3]

authenticator = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)

authenticator.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.api(authenticator, wait_on_rate_limit=True)


  