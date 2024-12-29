import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime

chatStr = ""

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio. Searching Google instead...")
        return "search_google"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "search_google"

if __name__ == "__main__":
    text = "Hello, I am Jarvis AI. How can I help you?"
    text_to_speech(text)
    while True:
        query = takeCommand()
        
        # Handle unknown voice recognition
        if query == "search_google" or query == "":
            text_to_speech("What should I search for?")
            query = takeCommand()
            if query:
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open(search_url)
                text_to_speech(f"Here are the search results for {query}")
            continue

        # Predefined sites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["youtube broken angel song", "https://www.youtube.com/watch?v=bC3WAxiLnDY&list=RDbC3WAxiLnDY&start_radio=1"]
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                text_to_speech(f"Opening {site[0]}, Siddu")
                webbrowser.open(site[1])
                break

        # Play music file locally
        if "open music" in query:
            musicPath = r"C:\Users\sidda\Downloads\KantaraSingaraSiriyeRingtoneMp31988810805.mp3"
            os.startfile(musicPath)

        # Search song on YouTube
        elif "play" in query or "song" in query:
            text_to_speech("Searching for the song on YouTube...")
            youtube_search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(youtube_search_url)
            text_to_speech(f"Here are the search results for {query} on YouTube")

        # Fetch current time
        elif "what's the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            second = datetime.datetime.now().strftime("%S")
            text_to_speech(f"Sir, the time is {hour} hour {minute} minutes {second} seconds")

        # Open VS Code
        elif "open vs code" in query:
            vs_code = r"c:\Users\sidda\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
            os.startfile(vs_code)

        # Static response for specific query
        elif "what is agriculture" in query:
            text_to_speech("Agriculture is the broad term for everything that goes into producing food and materials for people to use. This includes cultivating land, raising livestock, and harvesting crops.")

        # Exit the program
        elif "exit" in query:
            text_to_speech("Goodbye, Siddu.")
            exit()

        # General Google search for unknown query
        else:
            text_to_speech("Let me search that for you.")
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            text_to_speech(f"Here are the search results for {query}")
