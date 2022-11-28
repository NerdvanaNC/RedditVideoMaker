### Create a finished video ###
import os

from reddit import topComments, topPost
from audio import writeAudio
from screenshots import screenshot
from video import makeClip, makeVideo

# constants
VIDEO_PATH, AUDIO_PATH, IMAGE_PATH = 'video', 'audio', 'screenshots' # no trailing slashes

post = topPost()
comments = topComments(post)
clips = []

print('Using Post: {} - {}'.format(post.title, post.id))

postAudio = writeAudio(post.title, post.id, 'post')
postScreenshot = screenshot(post.url, post.id, 'post')
clips.append(makeClip(postAudio, postScreenshot))

for comment in comments:
  commentAudio, commentScreenshot = writeAudio(comment.body, comment.id, 'comment'), screenshot(comment.permalink, comment.id, 'comment')
  clips.append(makeClip(commentAudio, commentScreenshot))

  # Trying out videos with just top-level comments
  # subcommentAudio, subcommentScreenshot = writeAudio(comment.replies[0].body, '{}_{}'.format(comment.id, comment.replies[0].id), 'subcomment'), screenshot(comment.replies[0].permalink, '{}_{}'.format(comment.id, comment.replies[0].id), 'subcomment')
  # clips.append(makeClip(subcommentAudio, subcommentScreenshot))

makeVideo(clips, post.id) # make the video

# update completed posts log
with open('done_posts.txt', 'a') as file:
  file.write('{}\n'.format(post.id))

# delete all audio/screenshot files
for filename in os.listdir(AUDIO_PATH):
  audioFile = os.path.join(AUDIO_PATH, filename)
  screenshotFile = os.path.join(IMAGE_PATH, filename.replace('mp3', 'png'))
  os.remove(audioFile)
  os.remove(screenshotFile)