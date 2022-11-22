from gtts import gTTS
from pydub import AudioSegment

def writeAudio(text, objID, objType):
  tts = gTTS(text, lang='en', tld='com.au', slow=False)
  with open('audio/{}_{}.mp3'.format(objType, objID), 'wb') as f:
    tts.write_to_fp(f)
  
  snippet = AudioSegment.from_file('audio/{}_{}.mp3'.format(objType, objID), format='mp3')
  spedup = snippet.speedup(playback_speed=1.25)
  spedup.export('audio/{}_{}.mp3'.format(objType, objID))