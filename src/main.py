import tweepy
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

if __name__ == '__main__':
    client = create_twitter_client()
    
    if client:
        # Replace 'Twitter' with any Twitter username you'd like to test
        user = client.get_user(screen_name='Twitter')
        print(f"User: {user.name}")
        print(f"Followers: {user.followers_count}")
        print(f"Account Created: {user.created_at}")
