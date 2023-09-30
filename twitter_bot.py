# Dependencies
import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the environment key using os.getenv()
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# Tweet Ethereum Price
def tweet_ethereum_price(price):
    try:
        # Initialize the Twitter bot
        client = tweepy.Client(
            API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
        )
        auth = tweepy.OAuth1UserHandler(
            API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
        )
        # Keep API incase purchase of V2 api
        # api = tweepy.API(auth)

        # Tweet the price
        tweet_text = f"The price of Ethereum currently is: {price}"
        client.create_tweet(tweet_text)

        print(f"Tweeted: {tweet_text}")
    except Exception as e:
        print(f"Error: {e}")
