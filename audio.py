from google.cloud import texttospeech
# from better_profanity import profanity

def writeAudio(text, objID, objType):
  filename = 'audio/{}_{}.mp3'.format(objType, objID)
  tts = texttospeech.TextToSpeechClient()

  # profanity_filtered_text = profanity.censor(text, '-')
  cleaned_text = text.replace('*', '').replace('_', '')

  text = texttospeech.SynthesisInput(text=cleaned_text)
  voice = texttospeech.VoiceSelectionParams(language_code='en-AU', name='en-AU-Standard-B', ssml_gender=texttospeech.SsmlVoiceGender.MALE)
  audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

  response = tts.synthesize_speech(input=text, voice=voice, audio_config=audio_config)

  with open(filename, 'wb') as f:
    f.write(response.audio_content)

  return filename