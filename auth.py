from dotenv import load_dotenv
import os
import tweepy

load_dotenv()
BEARER = os.getenv("BEARER_TOKEN")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_api() -> tweepy.API:
    """
    Get the Twitter API
    
    Returns
    -------
    tweepy.API : tweepy.API
        Twitter API
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

if __name__=="__main__":
    auth = get_api()
    print(auth.me().name)
    print(auth.me().screen_name)
