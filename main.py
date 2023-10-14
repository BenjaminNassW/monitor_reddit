import praw
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Reddit API credentials
client_id = str(os.getenv('CLIENT_ID'))
client_secret = str(os.getenv('CLIENT_SECRET'))
user_agent = str(os.getenv('USER_AGENT'))
username = str(os.getenv('USERNAME_REDDIT'))
password = str(os.getenv('PASSWORD'))

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
)


for submission in reddit.subreddit("rickandmorty").hot(limit=10):
    print(submission.title) 
# Specify the subreddit to monitor
subreddit_name = 'rickandmorty'  # Change this to the specific subreddit you want

# Search query
search_query = 'Season 7'

# Monitor new submissions
subreddit = reddit.subreddit(subreddit_name)


""" for submission in subreddit.new(limit=20):
    if search_query.lower() in submission.title.lower():
        # You've found new information about Season 7, report it!
        print("New Season 7 information found:", submission.title)
        # Implement your reporting logic here (e.g., send a notification). """

search_queries = ['Season 7', 'S7', 'S07']  # Add your search queries here

for submission in subreddit.hot(limit=10):
    if any(query.lower() in submission.title.lower() for query in search_queries):
        # Found a match, do something
        print(f"Match found in post:", submission.title)

