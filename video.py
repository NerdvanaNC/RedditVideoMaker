from operator import attrgetter
import random
import os

import moviepy.editor as mp

# constants
W, H = 1080, 1920
VIDEO_PATH, AUDIO_PATH, IMAGE_PATH = 'video', 'audio', 'screenshots' # no trailing slashes

def makeClip(audioFile, screenshotFile):
  audioClip = mp.AudioFileClip(audioFile)
  screenshotClip = (mp.ImageClip(screenshotFile)
    .set_duration(audioClip.duration)
    .set_audio(audioClip)
    .resize(width=(W - 100))
    .set_opacity(0.9)
    .crossfadein(0.2)
    .crossfadeout(0.2)
  )

  return screenshotClip

def makeVideo(clipList, filename):
  startingPoint = random.randrange(1, 504) # Our source is 575s long - keeping a buffer of 70 seconds at the end (575-71=504) means we can subclip the video from any point in this range
  duration = 0

  for clip in clipList:
    duration += clip.duration

  while duration > 90:
    longestClip = max(clipList, key=attrgetter('duration'))
    duration -= longestClip.duration
    clipList.remove(longestClip)

  videoClip = (mp.VideoFileClip('{}/source.mp4'.format(VIDEO_PATH))
    .without_audio()
    .subclip(startingPoint, (startingPoint+duration))
    .resize(height=H)
    .crop(x1=1166.6, y1=0, x2=2246.6, y2=H) # crop video 1080x1920 (portrait); 2246.6-1166.6=1080
  )

  imageConcat = mp.concatenate_videoclips(clipList).set_position('center', 'center')
  mp.CompositeVideoClip([videoClip, imageConcat]).write_videofile('{}/{}.mp4'.format(VIDEO_PATH, filename))