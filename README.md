# Python Voice Assistant

A virtual voice assistant that can perform tasks like:
- **Opening websites** (Google, YouTube, Instagram, etc.)
- **Telling the time**
- **Searching Wikipedia**
- **Conversing with an AI chatbot**
- **Speech recognition and text-to-speech**

This assistant uses:
- **SpeechRecognition** for voice input
- **Google Text-to-Speech (gTTS)** for voice output
- **Wikipedia API** for information retrieval
- **Hugging Face Chatbot API** for AI conversations

---

## 🚀 Features
✔ **Voice-controlled commands**
✔ **AI-powered chatbot using Hugging Face API**
✔ **Wikipedia search integration**
✔ **Opens websites with voice commands**
✔ **Supports Windows, macOS, and Linux**
✔ **Works offline for speech recognition (except chatbot and Wikipedia search)**

---

## 📦 Installation

### **Step 1: Clone the Repository**
```sh
# Using Git
git clone https://github.com/Prajjwal2051/Python-Virtual-Assistant.git
cd Python-Virtual-Assistant
```

### **Step 2: Install Dependencies**
Install the required Python packages:
```sh
pip install -r requirements.txt
```
If you don’t have `pip`, install it using:
```sh
python -m ensurepip --default-pip
```

### **Step 3: Set Hugging Face API Key (Secure Method)**
To interact with the chatbot, set up your Hugging Face API key.

**Windows (Command Prompt):**
```cmd
set HUGGINGFACE_API_KEY=your_api_key_here
```
**Windows (PowerShell):**
```powershell
$env:HUGGINGFACE_API_KEY="your_api_key_here"
```
**Linux/macOS:**
```sh
export HUGGINGFACE_API_KEY="your_api_key_here"
```

---

## 🎤 How to Use

### **Run the Script**
```sh
python main.py
```

### **Voice Commands Available**
| Command | Function |
|---------|----------|
| "Open YouTube" | Opens YouTube in the browser |
| "What is the time?" | Tells the current time |
| "Wikipedia Elon Musk" | Searches Wikipedia for Elon Musk |
| "Who is the President of India?" | Asks AI chatbot |
| "Exit" or "Quit" | Stops the assistant |

---

## 🛠 Troubleshooting
**Issue:** Speech recognition is not working.  
**Solution:** Make sure your **microphone is working**, and try increasing `adjust_for_ambient_noise()` time.

**Issue:** `Hugging Face API` returns `401 Unauthorized`.  
**Solution:** Ensure your API key is correct and set in the environment variables.

**Issue:** `ModuleNotFoundError: No module named 'pydub'`.  
**Solution:** Install `ffmpeg`:
```sh
# Linux
sudo apt install ffmpeg

# macOS (using Homebrew)
brew install ffmpeg

# Windows
choco install ffmpeg
```

---

## 🤝 Contributing
1. **Fork the repo**
2. **Create a new branch** (`feature-new-command`)
3. **Commit your changes** (`git commit -m "Added new command"`)
4. **Push the branch** (`git push origin feature-new-command`)
5. **Create a Pull Request**

---

## 📜 License
This project is licensed under the **MIT License**.



🎯 Developed by Prajjwal Sahu

🚀 Happy Coding!

