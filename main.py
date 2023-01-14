import os
import tweepy

API_KEY = os.getenv("TWITTER_API_KEY", "NOT FOUND")
API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET", "NOT FOUND")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "NOT FOUND")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "NOT FOUND")


def post_tweet():
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    api.update_status("Hello, World!")


if __name__ == "__main__":
    post_tweet()