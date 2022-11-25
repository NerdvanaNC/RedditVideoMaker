from moviepy.editor import *
import os

# constants
W, H = 1080, 1920
VIDEO_PATH, AUDIO_PATH, IMAGE_PATH = 'video', 'audio', 'screenshots' # no trailing slashes

# audioClip = (AudioFileClip('{}/comment_ixexyvv.mp3'.format(AUDIO_PATH)))

# clip = (VideoFileClip('{}/source.mp4'.format(VIDEO_PATH))
#   .without_audio()
#   .subclip(200,(200+audioClip.duration+audioClip2.duration))
#   .resize(height=H)
#   .crop(x1=1166.6, y1=0, x2=2246.6, y2=H) # crop video 1080x1920 (portrait); 2246.6-1166.6=1080
#   .set_audio(audioClip)
#   )

# imgClip = (ImageClip('{}/comment_ixexyvv.png'.format(IMAGE_PATH))
#   .set_duration(audioClip.duration)
#   .resize(width=W - 100)
#   .set_position('center', 'center')
#   .set_opacity(0.8)
#   .crossfadein(0.2)
#   .crossfadeout(0.2)
#   )

# final = CompositeVideoClip([clip, imgClip])
# final.write_videofile('{}/test.mp4'.format(VIDEO_PATH))

def makeClip(audioFile, screenshotFile):
  audioClip = AudioFileClip(audioFile)
  screenshotClip = (ImageClip(screenshotFile)
    .set_duration(audioClip.duration)
    .set_audio(audioClip)
    .resize(width=(W - 100))
    .set_opacity(0.9)
    .crossfadein(0.2)
    .crossfadeout(0.2)
  )

  return screenshotClip

def makeVideo(clipList):
  duration = 0

  for clip in clipList:
    duration += clip.duration

  videoClip = (VideoFileClip('{}/source.mp4'.format(VIDEO_PATH))
    .without_audio()
    .subclip(200, (200+duration))
    .resize(height=H)
    .crop(x1=1166.6, y1=0, x2=2246.6, y2=H) # crop video 1080x1920 (portrait); 2246.6-1166.6=1080
  )

  imageConcat = concatenate_videoclips(clipList).set_position('center', 'center')
  CompositeVideoClip([videoClip, imageConcat]).write_videofile('{}/test.mp4'.format(VIDEO_PATH))