import praw
reddit = praw.Reddit('videoMaker')

def topPost():
  for post in reddit.subreddit('AskReddit').hot(limit=1):
    return post

def topComments():
  return topPost().comments[:5]