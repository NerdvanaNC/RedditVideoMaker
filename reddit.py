import praw
reddit = praw.Reddit('videoMaker')

def topPost(skipNum = 0):

  # recursion, but only upto a certain limit
  if skipNum >= 50:
    raise ResourceWarning('We haven\'t found a single usable post in 55 posts. Stopping here.')

  for post in reddit.subreddit('AskReddit').hot(limit=(skipNum + 5)):
    if not post.spoiler and not post.over_18:
      return post
  
  # if none of the posts we got were usable
  # we repeat the search and up the limit by another 5

  topPost((skipNum) + 5)

def topComments(post):
  return post.comments[:5]