import speech_recognition as sr
import webbrowser
import pyttsx3

from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()



def speak(text):
    engine.say(text)
    engine.runAndWait() 

def aiProcess(command):
      client = OpenAI(
      api_key="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"
      )

      completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
         {
               "role": "user",
               "content": command
         }
      ]
   )

      return completion.choices[0].message.content
   

def processCommand(c):
    if "open google" in c.lower():
       webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
       webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
       webbrowser.open("http://linkedin.com")
   
   



if __name__=="__main__":
    speak("Initializing jarvis....")
    while True:
    #listen to the wake word "Jarvis"
        r = sr.Recognizer()
        
        

        print("recognizing...")
        try:
            with sr.Microphone() as source:
              print("Listening..")
              audio = r.listen(source, timeout=2,phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                #listen to command
                with sr.Microphone() as source:
                 print("Jarvis active.")
                 audio = r.listen(source, timeout=2,phrase_time_limit=1)
                 command = r.recognize_google(audio)

                 processCommand(command)
        
        except Exception as e:
            print("error; {0}".format(e))
