import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3

# updated from os.espeak to pyttsx3 which works offline
def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source)  # Helps with background noise
        print("Listening...")
        r.pause_threshold = 1  # Pause before recognizing speech
        audio = r.listen(source)  # Must be inside the `with` block

    try:
        query = r.recognize_google(audio, language="en-in")  # Changed from Bing to Google
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return "I couldn't understand"
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return "Request failed"

# Main script
if __name__ == "__main__":
    say("Hello, from A.I ")
    print("Listening...")
    query = take_command()
    # say(query)

    # list of websites to be opened
    sites=[["youtube","https://youtube.com"],["instagram","https://instagram.com"],
           ["google","https://google.com"]]
    

    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            webbrowser.open(site[1])
            say(f"opening {site[0]} sir")
            print(f"opening {site[0]}...")

    if "the time" in query:
        hour=datetime.datetime.now().strftime("%H")
        mins=datetime.datetime.now().strftime("%M")

        print(f"{hour} Hrs, {mins} Mins")
        say(f"the time is {hour} hours and {mins} minutes")
