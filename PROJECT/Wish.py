import datetime
import SpeakPython
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        SpeakPython.speak("Good Morning!")
    elif hour>=12 and hour<18:
        SpeakPython.speak("Good Afternoon!")   
    else:
        SpeakPython.speak("Good Evening!")  
    SpeakPython.speak("hello, I am your MJ. Sir how may I help you")