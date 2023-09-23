import tweepy

# Set your Twitter API credentials
consumer_key = 'VhxCqB3NSnN6IQZ2xCwkrsi9x'
consumer_secret = 'ldkjN8OFJ83pPnew9dcmzN2KREV5N6wYsd2A2QLgx2hbtL0cwI'
access_token = '1647603270435721219-kEW5zFa1Zk4YMxlT1IXnf7UnLJx0EQ'
access_token_secret = 'VIWegellqxmWjLMC1rIKkAZ1CjqjoBEV3AC6bnmKcqWdd'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of Twitter usernames to search for
usernames = ['elonmusk', 'naman_makkar_']

try:
    # Loop through each username and fetch user information
    for username in usernames:
        user = api.get_user(screen_name=username)
        followers_count = user.followers_count
        user_name = user.name
        profile_url = f"https://twitter.com/{username}"

        # Print user information
        print(f"Username: {username}")
        print(f"Followers Count: {followers_count}")
        print(f"Name: {user_name}")
        print(f"Profile URL: {profile_url}")
        print('-' * 50)

except tweepy.TweepError as e:
    print(f"An error occurred: {e}")