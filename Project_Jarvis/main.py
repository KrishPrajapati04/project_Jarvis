import speech_recognition as sr
import musicLibrary
import webbrowser
import pyttsx3 # so that we can make the machine speak
# pip install pocketsphinx
import requests
from client_final import ask_jarvis
from gtts import gTTS
# import pygame
# import os

recognizer  = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "news_api"

def speak(text):
    engine.say(text)
    engine.runAndWait()



def aiProcess(command):
    try:
        response = ask_jarvis(command)
        print("Jarvis:", response)
        speak(response)
    except Exception as e:
        print("❌ Error in aiProcess:", e)
        speak("Sorry, something went wrong.")



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        # print(song)
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
      
        data = r.json()

        # Extract all titles into a list
        titles = [article["title"] for article in data.get("articles", [])]

        # Print the list of titles
        speak(titles)

    else:
        # Let openAI handle the case
        print("🔁 :", c)  # DEBUG
        # from client_openRouter import ask_jarvis
        try:
            response = ask_jarvis(c)
            print("Jarvis:", response)
            speak(response)
        except Exception as e:
            print("❌ AI Error:", e)
            speak("Sorry, I had trouble understanding.")
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
while True:
    # Listen for the wake word "Jarvis"
    # Obtain audio from the microphone
    r = sr.Recognizer()
    
    print("recognizing")
    # recognize speech using Sphinx
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source , timeout = 5,phrase_time_limit=5)#''',timeout=2 ,phrase_time_limit=2''')

        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            speak("Yaah, How can I help you?")
            # Listen for command
            with sr.Microphone() as source:
                print("Jarvis active")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)
                processCommand(command)
    except Exception as e:
        print(" Error; {0}".format(e))
