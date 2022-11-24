from moviepy.editor import *

# constants
W, H = 1080, 1920
VIDEO_PATH, AUDIO_PATH, IMAGE_PATH = 'video', 'audio', 'screenshots' # no trailing slashes

audioClip = (AudioFileClip('{}/comment_ixexyvv.mp3'.format(AUDIO_PATH)))

clip = (VideoFileClip('{}/source.mp4'.format(VIDEO_PATH))
  .without_audio()
  .subclip(200,(200+audioClip.duration))
  .resize(height=H)
  .crop(x1=1166.6, y1=0, x2=2246.6, y2=H) # crop video 1080x1920 (portrait); 2246.6-1166.6=1080
  .set_audio(audioClip)
  )

imgClip = (ImageClip('{}/comment_ixexyvv.png'.format(IMAGE_PATH))
  .set_duration(audioClip.duration)
  .resize(width=W - 100)
  .set_position('center', 'center')
  .set_opacity(0.8)
  .crossfadein(0.2)
  .crossfadeout(0.2)
  )

final = CompositeVideoClip([clip, imgClip])
final.write_videofile('{}/test.mp4'.format(VIDEO_PATH))