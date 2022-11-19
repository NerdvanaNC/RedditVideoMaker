### Create a finished video ###

from reddit import topComments, topPost
from audio import writeAudio
from screenshots import screenshot

## Reddit

screenshot(topPost()) # Get top post from AskReddit

for comment in topComments(): # Get top comments
  writeAudio(comment) # TTS
  screenshot(comment) # Playwright

## TTS
# Take comment texts from Reddit and save .mp3 snippets

## Playwright
# Take comment links from Reddit and save screenshots

## MoviePy
# Stitch together the screenshots and TTS clips over a background video.
# Handle timing and other logic
# Export completed file