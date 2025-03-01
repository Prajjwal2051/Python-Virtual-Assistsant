# importing the required modules and packages
import speech_recognition as sr
import os
import webbrowser
import datetime
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import wikipedia
from huggingface_hub import InferenceClient

API_KEY = os.getenv("HF_API_KEY")

client=InferenceClient(
    provider="hf-inference",
    api_key=API_KEY
)

def chat_with_bot(query):
    messages=[
        {"role":"user","content":query}
    ]

    completion=client.chat.completions.create(
        model="HuggingFaceH4/zephyr-7b-alpha",
        messages=messages,
        max_tokens=100
    )

    return completion.choices[0].message["content"]


def search_wikipedia(query):
    try:
        result=wikipedia.summary(query,sentences=2)
        print(result)
        say(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print("too many results, please be more specific")
        say("too many results, please be more specific")
    except wikipedia.exceptions.PageError:
        print("sorry, I couldn't find anything")
        say("sorry, I couldn't find anything")

# updated from os.espeak to pyttsx3 which works offline
# updating it to now google text to speech to make it sound more natural
def say(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    audio = AudioSegment.from_mp3("response.mp3")
    
    try:
        play(audio)
    finally:
        os.remove("response.mp3")  # Ensures cleanup even if an error occurs


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source)  # Helps with background noise
        r.dynamic_energy_threshold = True
        print("Listening...")
        r.pause_threshold = 1.5  # Pause before recognizing speech
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
    say("Hello, from Linux ")
    print("hello, from linux")
    while True: 
        query = take_command()
        # say(query)

        # list of websites to be opened
        sites=[
            
            ["youtube","https://youtube.com"],["instagram","https://instagram.com"],
            ["google","https://google.com"],["music","https://music.youtube.com"]
            
            ]
        

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

        if "wikipedia" in query.lower():
            search_query=query.lower().replace("wikipedia","").strip()
            search_wikipedia(search_query)


        if "exit" in query.lower() or "quit" in query.lower() or "stop" in query.lower():
            say("Goodbye!")
            break

        else:
            bot_response=chat_with_bot(query)
            print("AI:",bot_response)
            say(bot_response)