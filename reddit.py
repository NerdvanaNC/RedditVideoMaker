import praw
reddit = praw.Reddit('videoMaker')

def topPost():
  with open('done_posts.txt', 'r') as f:
    content = f.read()
  
  for post in reddit.subreddit('AskReddit').hot(limit=20):
    if not post.spoiler and not post.over_18 and not post.stickied and not post.id in content:
      return post
  
  raise ResourceWarning('We haven\'t found a single usable post in 20 posts. Stopping here.')

def topComments(post):
  post.comments.replace_more(limit=10)

  finalComments = []
  for comment in post.comments:
    if not '>' in comment.body:
      finalComments.append(comment)
  
  return finalComments[:5]