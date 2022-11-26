from gtts import gTTS
from pydub import AudioSegment
from better_profanity import profanity

def writeAudio(text, objID, objType):
  filename = 'audio/{}_{}.mp3'.format(objType, objID)

  tts = gTTS(profanity.censor(text, '-'), lang='en', tld='com.au', slow=False)
  with open(filename, 'wb') as f:
    tts.write_to_fp(f)
  
  snippet = AudioSegment.from_file(filename, format='mp3')
  spedup = snippet.speedup(playback_speed=1.2)
  spedup.export(filename)

  return filename