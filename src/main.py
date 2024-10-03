import os
import tweepy
import requests
from datetime import datetime
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

def create_twitter_client_v2():
    """
    Creates and returns a Tweepy client object using Twitter API v2 credentials.
    """
    client = tweepy.Client(bearer_token=TWITTER_ACCESS_TOKEN)
    
    if client:
        print("Twitter API v2 connection established successfully!")
        return client
    else:
        print("Error during authentication.")
        return None

def save_media(url, media_dir, filename):
    """
    Saves media from the given URL to the specified directory.
    """
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(media_dir, filename), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Saved media: {filename}")
    else:
        print(f"Failed to download media from {url}")

def fetch_media_from_tweets_v2(client, query, media_type='both', start_time=None, end_time=None):
    """
    Fetches tweets containing media from Twitter API v2 based on a query.
    
    Parameters:
    - query: search query (e.g. from:username)
    - media_type: 'images', 'videos', or 'both'
    - start_time: 'YYYY-MM-DDTHH:mm:ssZ' ISO 8601 string to filter tweets after this time
    - end_time: 'YYYY-MM-DDTHH:mm:ssZ' ISO 8601 string to filter tweets before this time
    """
    media_dir = 'media'
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

    # Search tweets based on the query
    tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at'], expansions=['attachments.media_keys'], media_fields=['url'])

    for tweet in tweets.data:
        # Process attached media
        if 'attachments' in tweet:
            media_keys = tweet.attachments['media_keys']
            for media in client.media(media_keys=media_keys).data:
                media_url = media.get('url')
                if media_url:
                    filename = os.path.basename(media_url)
                    
                    # Save the media
                    save_media(media_url, media_dir, filename)

if __name__ == '__main__':
    # Create Twitter API v2 client
    client = create_twitter_client_v2()
    
    if client:
        # Replace with a search query, e.g. 'from:username'
        fetch_media_from_tweets_v2(
            client, 
            query='from:TwitterDev',  # Replace with a valid query
            media_type='both',
            start_time='2023-01-01T00:00:00Z',  # Adjust as needed
            end_time='2024-01-01T00:00:00Z'     # Adjust as needed
        )
