from gtts import gTTS
from pydub import AudioSegment

def writeAudio(comment):
  tts = gTTS(comment.body, lang='en', tld='com.au', slow=False)

  with open('audio/{}.mp3'.format(comment.id), 'wb') as f:
    tts.write_to_fp(f)
  
  snippet = AudioSegment.from_file('audio/{}.mp3'.format(comment.id), format='mp3')
  spedup = snippet.speedup(playback_speed=1.25)
  snippet.export('audio/{}.mp3'.format(comment.id))
  spedup.export('audio/{}_fast.mp3'.format(comment.id))