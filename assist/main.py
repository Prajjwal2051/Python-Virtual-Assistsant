import speech_recognition as sr
import os

def say(text):
    os.system(f'espeak "{text}"')

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
    text = take_command()
    say(text)
