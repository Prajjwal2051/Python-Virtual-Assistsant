# Python Virtual Assistant

This is a Python-based **voice assistant** that can recognize speech, search Wikipedia, open websites, tell the time, and even chat using Hugging Face's **Zephyr-7B** chatbot.

---

## 🔧 Features
- **Speech Recognition** 🎧 (Uses Google Speech API)  
- **Text-to-Speech (TTS)** 🔊 (Using Google TTS)  
- **Wikipedia Search** 📚  
- **Website Shortcuts** 🌐 (Easily open sites like YouTube, Google, etc.)  
- **AI Chatbot** 🤖 (Hugging Face’s Zephyr-7B)  

---

## 📌 Installation Guide (Step-by-Step)
Follow these steps to **set up and run the assistant** on your system.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Prajjwal2051/Python-Virtual-Assistsant.git
cd Python-Virtual-Assistsant
```

---

### **2️⃣ Create a Virtual Environment**
```bash
python3 -m venv assist
```
- **(Optional) If using fish shell:**
  ```bash
  set -gx VIRTUAL_ENV assist
  set -gx PATH $VIRTUAL_ENV/bin $PATH
  ```

---

### **3️⃣ Activate the Virtual Environment**
- **For Bash/Zsh:**  
  ```bash
  source assist/bin/activate
  ```
- **For Fish shell:**  
  ```bash
  source assist/bin/activate.fish
  ```

---

### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

> 🚀 If you are using **GPU (CUDA)**, install PyTorch manually:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

### **5️⃣ Run the Virtual Assistant**
```bash
python main.py
```

---

## 📝 How to Use
1. **Start the assistant** and wait for it to greet you.  
2. **Give voice commands** like:  
   - `"Open YouTube"`  
   - `"Search Wikipedia for Python"`  
   - `"What is the time?"`  
3. **Chat with the AI** by speaking normally.  
4. The assistant will respond via **text-to-speech** and **text output**.  

---

## 📢 Troubleshooting

### 🔴 Error: `externally-managed-environment`
- Use a **virtual environment** (`venv`) before installing dependencies.
  
### 🔴 PyAudio Compilation Error
- Install missing dependencies:
  ```bash
  sudo apt update
  sudo apt install portaudio19-dev
  ```

### 🔴 Model Not Found on Hugging Face
- Make sure **transformers** and **accelerate** are installed:
  ```bash
  pip install transformers accelerate
  ```

---

## 🤝 Contributing
Feel free to **fork**, make changes, and submit a **pull request (PR)**.

---

## 📜 License
This project is open-source under the **MIT License**.


🎯 Developed by Prajjwal Sahu

🚀 Happy Coding!

