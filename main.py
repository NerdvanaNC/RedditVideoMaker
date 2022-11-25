### Create a finished video ###

from reddit import topComments, topPost
from audio import writeAudio
from screenshots import screenshot
from video import makeClip, makeVideo

post = topPost()
comments = topComments(post)
clips = []

postAudio = writeAudio(post.title, post.id, 'post')
postScreenshot = screenshot(post.url, post.id, 'post')
clips.append(makeClip(postAudio, postScreenshot))

for comment in comments:
  commentAudio, commentScreenshot = writeAudio(comment.body, comment.id, 'comment'), screenshot(comment.permalink, comment.id, 'comment')
  clips.append(makeClip(commentAudio, commentScreenshot))
  subcommentAudio, subcommentScreenshot = writeAudio(comment.replies[0].body, '{}_{}'.format(comment.id, comment.replies[0].id), 'subcomment'), screenshot(comment.replies[0].permalink, '{}_{}'.format(comment.id, comment.replies[0].id), 'subcomment')
  clips.append(makeClip(subcommentAudio, subcommentScreenshot))

makeVideo(clips)