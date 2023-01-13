### Create a finished video ###
import os

from reddit import topComments, topPosts
from audio import writeAudio
from screenshots import screenshot
from video import makeClip, makeVideo

# constants
VIDEO_PATH, AUDIO_PATH, IMAGE_PATH = 'video', 'audio', 'screenshots' # no trailing slashes


listOfPosts = topPosts()
print("Here are the top 5 posts:")
for i in range(len(listOfPosts)):
  print('[{}] - {}'.format(i, listOfPosts[i].title))
postInput = input('Which post do you want to use? Enter the number in the [brackets]: ')
print('\nGot it!\n')

post = listOfPosts[int(postInput)]
comments = topComments(post)

print('Using Post: {} - {}'.format(post.title, post.id))

comments = topComments(post)
clips = []

postAudio = writeAudio(post.title, post.id, 'post')
postScreenshot = screenshot(post.url, post.id, 'post')
clips.append(makeClip(postAudio, postScreenshot))

for comment in comments:
  commentAudio, commentScreenshot = writeAudio(comment.body, comment.id, 'comment'), screenshot(comment.permalink, comment.id, 'comment')
  clips.append(makeClip(commentAudio, commentScreenshot))

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