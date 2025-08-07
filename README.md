🤖 JOVA AI - Your Personal Voice Assistant
JOVA AI is a Python-based voice assistant that acts like your personal Jarvis. It combines speech recognition, mood-based TTS responses, AI-driven replies via the Groq API, real-time news and weather, YouTube music, and more. Think of it as a mini-Alexa powered by Python.

* 🧠 Features
* 🎙️ Voice recognition with wake word ("Jarvis")
* 😃 Mood-based text-to-speech responses
* 🌐 Answers questions using Groq's LLaMA-3 AI model
* 🔊 Plays music from YouTube
* 🌦️ Fetches real-time weather info (OpenWeather API)
* 📰 Reads top news headlines (NewsAPI)
* ⏱️ Set timers and alarms using your voice
* 🗣️ Tells jokes, flips coins, rolls dice
* 📝 Remembers user notes
* 💻 Opens websites like Google, YouTube, Instagram, GitHub, etc.
* 👻 Includes fun features like creepy mode, roasts, lie detection

📁 Project Structure
JOVA_AI/
│
├── main.py         # Core logic, command processing, speech handling
├── client.py       # API configuration for Groq's AI model
├── music.py        # List of preloaded YouTube music links
└── reminders.txt   # Stores "remember" commands (auto-generated)

🛠️ Requirements
Install these Python packages before running the project:
pip install speechrecognition pyttsx3 gTTS pygame requests pywhatkit

Also install the required dependencies for speechrecognition:
pip install pyaudio

🔑 API Keys Required
Create accounts and get free API keys from:
* Groq API: For AI responses — https://console.groq.com
* OpenWeather API: For weather updates — https://openweathermap.org/api
* News API: For headlines — https://newsapi.org
Place the keys in main.py as shown:
newsapi = "YOUR_NEWS_API_KEY"
weather_api_key = "YOUR_WEATHER_API_KEY"
GROQ_API_KEY = "YOUR_GROQ_API_KEY"

🚀 How to Run
1. Plug in your microphone.
2. Open terminal in project folder.
3. Run the assistant:
   # python main.py
4. Say “Jarvis” to activate it, then give commands like:
   * “What’s the weather in Delhi?”
   * “Play Alan Walker faded”
   * “Tell me a joke”
   * “Open YouTube”
   * “Set alarm for 14:00"
   * “What do you remember?”

💡 Future Ideas
   * GUI using Tkinter or PyQt
   * Voice training personalization
   * Integration with home automation APIs
   * Advanced emotion detection



