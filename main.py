import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.environ["API_KEY"]
API_KEY_SECRET=os.environ["API_KEY_SECRET"]
ACCESS_TOKEN=os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET=os.environ["ACCESS_TOKEN_SECRET"]

authenticator = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)

authenticator.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(authenticator)

# api.create_friendship("novicetopro254")


# followers = api.get_followers()

# api.update_status("C# is a god tbh")

try:
    api.verify_credentials()
    print("It's working alright")
except:
    print("Figure it out")
 

print(f"")