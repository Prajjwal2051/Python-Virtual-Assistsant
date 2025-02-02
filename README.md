Virtual Assistant using Python

This is a Python-based virtual assistant that uses speech recognition and text-to-speech (TTS) capabilities. It can recognize voice commands, respond verbally, and open websites. Additionally, it can provide the current time and execute various other functionalities based on voice input.

🚀 Features

Speech Recognition: Uses speech_recognition to recognize spoken commands.

Text-to-Speech (TTS): Uses gTTS (Google Text-to-Speech) to provide responses.

Audio Playback: Uses pydub to play back generated speech.

Web Navigation: Can open popular websites like YouTube, Google, and Instagram.

Time Query: Responds with the current time when asked.

Noise Reduction: Adjusts for ambient noise before listening to commands.

Error Handling: Provides user-friendly messages for unrecognized speech or request failures.

🔧 Installation & Setup

1️⃣ Create & Activate Virtual Environment

python3 -m venv assist
source assist/bin/activate  # For Linux/macOS
assist\Scripts\activate    # For Windows (PowerShell)

2️⃣ Install Required Packages

pip install speechrecognition gtts pydub webbrowser datetime

3️⃣ Install System Dependencies

sudo apt install portaudio19-dev ffmpeg alsa-utils jackd2 -y
pip install pyaudio

4️⃣ Run the Virtual Assistant

python main.py

📌 How It Works

The assistant listens for a voice command.

It recognizes the command and processes the request.

If a website needs to be opened, it uses webbrowser.open().

If the user asks for the time, it retrieves the current time and speaks it out.

The response is converted into speech using gTTS and played using pydub.

🔄 Changes & Fixes Implemented

✅ Fixed AttributeError: Could not find PyAudio

Installed missing dependency:

sudo apt install portaudio19-dev
pip install pyaudio

✅ Replaced os.system speech output with gTTS for better TTS

Used gtts instead of espeak for more natural-sounding speech

✅ Replaced recognize_bing with recognize_google

Removed API key requirement by using Google Speech Recognition

✅ Fixed FileNotFoundError: No such file or directory: 'ffprobe'

Installed ffmpeg:

sudo apt install ffmpeg

✅ Fixed ALSA / JACK Server Warnings

Suppressed unnecessary logs using:

python3 main.py 2>/dev/null

Installed and restarted ALSA if needed:

sudo apt install alsa-utils jackd2
sudo alsa force-reload

📌 Usage Examples

"Open YouTube" → Opens YouTube in the browser

"What is the time?" → Tells the current time

Other queries → Responds using TTS

📌 Future Improvements

Add weather updates using an API.

Integrate a chatbot for better interactions.

Automate system tasks such as opening applications.

Improve speech recognition accuracy with NLP models.

🎯 Developed by Prajjwal Sahu

🚀 Happy Coding!

