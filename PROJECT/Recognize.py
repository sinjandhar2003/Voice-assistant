import speech_recognition as sr   
def recognize():                                                      
            r = sr.Recognizer()                                                                                   
            with sr.Microphone() as source:                                                                       
                print("Speak...")                                                            
                audio = r.listen(source) 
                r.energy_threshold = 400
            try:
                query = r.recognize_google(audio , language="en-in")
                print("You said " +query)
            except:
                return "none"
            return query    