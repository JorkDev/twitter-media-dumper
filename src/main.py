import os
import tweepy
import requests
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

def create_twitter_client():
    """
    Creates and returns a Tweepy client object using the credentials.
    """
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_SECRET
    )
    client = tweepy.API(auth)
    
    try:
        client.verify_credentials()
        print("Twitter API connection established successfully!")
        return client
    except tweepy.TweepError as e:
        print(f"Error during authentication: {e}")
        return None

def save_media(url, media_dir, filename):
    """
    Saves media from the given URL to the specified directory.
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(media_dir, filename), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Saved media: {filename}")
    else:
        print(f"Failed to download media from {url}")

def fetch_media_from_tweets(client, screen_name):
    """
    Fetches the latest tweets from the user and saves media (photos, videos) locally.
    """
    tweets = client.user_timeline(screen_name=screen_name, count=20, tweet_mode='extended')
    
    media_dir = 'media'
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)
    
    for tweet in tweets:
        media = tweet.entities.get('media', [])
        if media:
            for media_item in media:
                media_url = media_item['media_url_https']
                filename = os.path.basename(media_url)
                save_media(media_url, media_dir, filename)

if __name__ == '__main__':
    client = create_twitter_client()
    
    if client:
        # Replace 'Twitter' with any username you'd like to fetch media from
        fetch_media_from_tweets(client, screen_name='Twitter')
