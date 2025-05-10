# Import necessary libraries
import webbrowser
# import google
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
# import os
import smtplib
import datetime
import random

# List of Spotify playlist URLs (replace with your own playlists)
spotify_playlists = [
    "https://open.spotify.com/collection/tracks",
    "https://open.spotify.com/playlist/37i9dQZF1E36Ax18lPwcVg",
]
# Define a function to speak text
def speak(audio):
    # Initialize speech engine
    engine = pyttsx3.init()
    # Set the voice

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ROBERT_11.0')
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)

    # Set the speech rate to slow
    engine.setProperty('rate', 190)
    engine.say(audio)
    engine.runAndWait()

# Define a function to take voice commands
def takeCommand():
    # Initialize speech recognition engine
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User  said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Define a function to wish the user
def wishMe():
    # Get current hour
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")   
        speak("Good Afternoon!")
    else:
        print("Good Evening!")   
        speak("Good Evening!")
    print("I am Rizzler Sir. Please tell me how may I help you")              
    speak("I am Rizzler Sir. Please tell me how may I help you")

# Define a function to send an email
def sendEmail(to, content):
    # Initialize SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Main program
if __name__ == "__main__":
    # Wish the user
    wishMe()
    while True:
        # Take a voice command
        query = takeCommand().lower()
        
        # Check if user wants to search Wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()  # Remove "Wikipedia" from the query and strip any leading/trailing whitespace
            if query:  # Check if the query is not empty
                results = wikipedia.summary(query, sentences=5)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            else:
                speak("Please specify a topic to search for on Wikipedia")

        
        #checks if user wants to search google
        elif 'google' in query:
            speak('Searching Google...')
            query = query.replace("google", "").strip()  # Remove "Google" from the query and strip any leading/trailing whitespace
            if query:  # Check if the query is not empty
                url = "https://www.google.com/search?q=" + query
                webbrowser.open(url)
                speak("Google search results are open in your default browser")
            else:
                speak("Please specify a topic to search for on Google")

        # Check if user wants to open YouTube
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            url = "https://www.youtube.com"
            webbrowser.open(url)
            speak("Youtube is now open")
        
        # Check if user wants to open Google
        elif 'open google' in query:
            speak("Opening Google...")
            url = "https://www.google.com"
            webbrowser.open(url)
            speak("Google is now open")
        
        # Check if user wants to open GitHub
        elif 'open github' in query:
            speak("Opening GitHub...")
            url = "https://github.com"
            webbrowser.open(url)
            speak("GitHub is now open")
        
        # Check if user wants to open Google Drive
        elif 'open drive' in query:
            speak("Opening Google Drive...")
            url = "https://drive.google.com"
            webbrowser.open(url)
            speak("Google Drive is now open")
        
        # Check if user wants to open Stack Overflow
        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow...")
            url = "https://stackoverflow.com"
            webbrowser.open(url)
            speak("Stack Overflow is now open")
        
        # Check if user wants to play music
        elif 'play music' in query:
            speak("Playing music...")
            music_path = "/Users/admin/Desktop/manojstudy/manojstudy/pythonprog/songs/audio.mp3"  # Replace with your music file path
            try:
                import subprocess
                music_process = subprocess.Popen(['open', '-a', 'Music', music_path])  # Opens with the default music player on macOS
                speak("Music is now playing")
            except Exception as e:
                speak("Error playing music: " + str(e))
        
        # Check if user want to play random music
        elif 'open random spotify playlist' in query:
            speak("opening random spotify playlist...")
            try:
                # Select a random playlist from the list
                random_playlist = random.choice(spotify_playlists)
                # Open the playlist in the default web browser
                webbrowser.open(random_playlist)
                speak("A random playlist is now open on Spotify")
            except Exception as e:
                speak("Sorry, I couldn't open Spotify. Please try again.")
                print(f"Error: {e}")

        # Check if user wants to know the time
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        
        # Check if user wants to send an email
        elif 'email to manoj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "manojchoudhary7.in@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Manoj bhai. I am not able to send this email")    
        

        # Check if user wants to open Visual Studio Code
        elif 'open code' in query:
            speak("Opening code in Visual Studio Code...")
            codePath = "/Users/admin/Desktop/manojstudy/manojstudy/pythonprog/main.txt"
            try:
                import subprocess
                subprocess.call(['open', '-a', 'Visual Studio Code', codePath])
                speak("Code is now open")
            except Exception as e:
                speak("Error opening code: " + str(e))

        # Check if user wants to exit
        elif 'exit' in query:
            print("Goodbye Sir! have a nice day!")
            speak("Goodbye Sir! have a nice day!")
            break
        
        # If none of the above conditions are met
        else:
            speak("Sorry, I didn't understand that. Please repeat again")