import os
import tweepy
import requests
from datetime import datetime
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

def fetch_media_from_tweets(client, screen_name, media_type='both', start_date=None, end_date=None):
    """
    Fetches tweets from the user's timeline and saves media based on the type and date range.
    
    Parameters:
    - media_type: 'images', 'videos', or 'both'
    - start_date: 'YYYY-MM-DD' string to filter tweets after this date
    - end_date: 'YYYY-MM-DD' string to filter tweets before this date
    """
    tweets = client.user_timeline(screen_name=screen_name, count=100, tweet_mode='extended')
    
    media_dir = 'media'
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    for tweet in tweets:
        # Parse tweet date
        tweet_date = tweet.created_at
        
        # If a date range is provided, filter the tweets by the date range
        if start_date and tweet_date < datetime.strptime(start_date, '%Y-%m-%d'):
            continue
        if end_date and tweet_date > datetime.strptime(end_date, '%Y-%m-%d'):
            continue
        
        # Check for media in the tweet
        media = tweet.entities.get('media', [])
        if media:
            for media_item in media:
                media_url = media_item['media_url_https']
                filename = os.path.basename(media_url)
                
                # Filter by media type
                if media_type == 'images' and media_item['type'] != 'photo':
                    continue
                if media_type == 'videos' and media_item['type'] != 'video':
                    continue

                # Save the media
                save_media(media_url, media_dir, filename)

if __name__ == '__main__':
    # Create Twitter API client
    client = create_twitter_client()
    
    if client:
        # Replace with any username you'd like to fetch media from
        # Also replace media_type ('images', 'videos', 'both') and date range
        fetch_media_from_tweets(
            client, 
            screen_name='Twitter', 
            media_type='both', 
            start_date='2024-01-01', 
            end_date='2024-12-31'
        )
