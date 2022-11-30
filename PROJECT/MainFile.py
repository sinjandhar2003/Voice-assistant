import datetime
from datetime import date
from pynput.keyboard import Key,Controller
import time
import Recognize
import SpeakPython
import pywhatkit as kt
import wikipedia
import Wish
import AppOpen
import os
import SpeakPython   
if __name__ == "__main__":
    Wish.wishMe()
    while 'true':
            query = Recognize.recognize().lower()
            file_object = open('recordedText.txt','a')
            file_object.write(query)
            file_object.write('\n')
            file_object.close()
            if 'how are you' in query:
                SpeakPython.speak("i am fit and fine")
            elif 'on youtube' in query:
                query = query.replace("on youtube","")
                SpeakPython.speak("Playing on YouTube")
                kt.playonyt(query)
            elif 'on wikipedia' in query:
                query = query.replace("on wikipedia","")
                SpeakPython.speak("Searching on Wikipedia")
                s = wikipedia.summary(query,2)
                print(s)
                SpeakPython.speak(s)
            elif 'search' in query and 'on google' in query:
                query = query.replace("search","")
                query = query.replace("on google","")
                kt.search(query)
            elif 'open' in query:
                query = query.replace("open","")
                SpeakPython.speak("opening" + query)
                AppOpen.automation(query)
            elif 'stop' in query:
                break
            elif 'show me the history' in query:
                os.popen('recordedText.txt','w')
            elif 'who created you' in query:
                SpeakPython.speak("I have been created by Hritom Bhattacharya, Sinjan Dhar and Dipdyuti chakraborty")
            elif 'what is the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                SpeakPython.speak(f"Sir, the time is {strTime}")
            elif 'close' in query:
                SpeakPython.speak("Closing..")
                keyboard = Controller()
                with keyboard.pressed(Key.alt):
                    keyboard.press(Key.f4)
                    keyboard.release(Key.f4)
            elif 'introduce yourself' in query:
                SpeakPython.speak("I am your personal assistant, MJ. I was born on 3rd September 2022. I am developed by Hritom Bhattacharya, Sinjan Dhar and Dipdyuti chakraborty")
            else:
                print("Please try saying something else")
                continue