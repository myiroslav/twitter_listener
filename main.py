from dotenv import load_dotenv
import os
import tweepy

load_dotenv()
BEARER = os.getenv("BEARER")

if __name__ == "__main__":
    print(BEARER)