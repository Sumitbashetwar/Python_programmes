#!pip install playsound
#!pip install pygobject
#!pip install gtts


import playsound
from playsound import playsound
from gtts import gTTS 
def playaudio(audio):
  playsound(audio)
def audio_bana(text):
  audio=gTTS(text)
  audio.save("textaudio.mp3")
  playaudio("textaudio.mp3")
  audio_bana("Hi Myself Sumit Bashetwar")
  