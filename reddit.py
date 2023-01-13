import praw
reddit = praw.Reddit('videoMaker')

def topPosts():
  with open('done_posts.txt', 'r') as f:
    content = f.read()
  
  post_list = []
  
  for post in reddit.subreddit('AskReddit').hot(limit=20):
    if len(post_list) == 5:
      return post_list
    else:
      if not post.spoiler and not post.over_18 and not post.stickied and not post.id in content:
        post_list.append(post)
  
  raise ResourceWarning('We haven\'t found a single usable post in 20 posts. Stopping here.')

def topComments(post):
  post.comments.replace_more(limit=10)

  finalComments = []
  for comment in post.comments:
    if not '>' in comment.body and not 'http' in comment.body:
      finalComments.append(comment)
  
  return finalComments if len(finalComments) <= 8 else finalComments[:8]