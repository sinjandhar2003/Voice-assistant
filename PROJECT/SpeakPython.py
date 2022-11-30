from gtts import gTTS
import os
import playsound
voice=""
def speak(voice):
    tts = gTTS(voice)
    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)