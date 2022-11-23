### Create a finished video ###

from reddit import topComments, topPost
from audio import writeAudio
from screenshots import screenshot

post = topPost()
comments = topComments(post)

writeAudio(post.title, post.id, 'post')
screenshot(post.url, post.id, 'post')

for comment in comments:
  writeAudio(comment.body, comment.id, 'comment')
  screenshot(comment.permalink, comment.id, 'comment')
  writeAudio(comment.replies[0].body, '{}_{}'.format(comment.id, comment.replies[0].id), 'subcomment')
  screenshot(comment.replies[0].permalink, '{}_{}'.format(comment.id, comment.replies[0].id), 'subcomment')

## MoviePy
# Stitch together the screenshots and TTS clips over a background video.
# Handle timing and other logic
# Export completed file