import praw

# Reddit API credentials
client_id = '7EwyFAbL15YvTz7AuowC3Q'
client_secret = 's0FGnRQEqx8dxXv1LxN0GHO7js8rKg'
user_agent = 'sample.script.1.0.0'
username = 'Boco_the_chocobo'
password = 'Martin070517'

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
)

""" for submission in reddit.subreddit("rickandmorty").hot(limit=10):
    print(submission.title) """
# Specify the subreddit to monitor
subreddit_name = 'rickandmorty'  # Change this to the specific subreddit you want

# Search query
search_query = 'Season 7'

# Monitor new submissions
subreddit = reddit.subreddit(subreddit_name)


for submission in subreddit.new(limit=10):
    if search_query.lower() in submission.title.lower():
        # You've found new information about Season 7, report it!
        print("New Season 7 information found:", submission.title)
        # Implement your reporting logic here (e.g., send a notification).
