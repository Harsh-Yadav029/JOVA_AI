import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
import os
import datetime
import pywhatkit
import random
import time


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "789ae88c3f8c471ca11812a4cfc3461b"
weather_api_key = "78097d3676618954301fcc475dcb2cdd"

GROQ_API_KEY = "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"
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

moods = ["happy", "sad", "angry", "excited"]
current_mood = random.choice(moods)

def speak(text):
    try:
        tts = gTTS(text)
        tts.save('temp.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('temp.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    except Exception as e:
        print(f"Speak error: {e}")

def speak_with_mood(text):
    mood = current_mood
    if mood == "angry":
        text = f"I'm not in the mood, but... {text}"
    elif mood == "happy":
        text = f"Yay! {text}"
    elif mood == "sad":
        text = f"*sigh* {text}"
    speak(text)

def aiProcess(command):
    try:
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks."},
                {"role": "user", "content": command}
            ],
            "temperature": 0.7
        }
        response = requests.post(GROQ_ENDPOINT, headers=HEADERS, json=payload)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return "Sorry, I couldn't process that."
    except Exception as e:
        return f"AI Error: {e}"

def processCommand(c):
    c = c.lower()

    if "shutdown" in c:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    elif "restart" in c:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    elif "open" in c:
        sites = {
            "google": "https://google.com",
            "facebook": "https://facebook.com",
            "youtube": "https://youtube.com",
            "linkedin": "https://linkedin.com",
            "twitter": "https://twitter.com",
            "github": "https://github.com",
            "instagram": "https://instagram.com",
            "stackoverflow": "https://stackoverflow.com",
            "whatsapp": "https://web.whatsapp.com",
            "gmail": "https://mail.google.com",
            "reddit": "https://reddit.com",
            "spotify": "https://spotify.com",
            "amazon": "https://amazon.com",
            "netflix": "https://netflix.com",
            "quora": "https://quora.com",
            "stack exchange": "https://stackexchange.com",
            "codepen": "https://codepen.io"
        }
        for key in sites:
            if key in c:
                webbrowser.open(sites[key])
                return

    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Failed to fetch news.")

    elif "weather" in c:
        speak("Which city?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            city = recognizer.recognize_google(audio)

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            r = requests.get(url)
            data = r.json()
            
            if data.get("main"):
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                speak(f"The temperature in {city} is {temp}°C with {desc}")
            else:
                speak("Couldn't fetch the weather.")

    elif "remember" in c:
        task = c.replace("remember", "").strip()
        with open("reminders.txt", "a") as f:
            f.write(task + "\n")
        speak("I have noted that down.")

    elif "what do you remember" in c:
        try:
            with open("reminders.txt", "r") as f:
                notes = f.read()
            speak("Here's what you asked me to remember: " + notes)
        except FileNotFoundError:
            speak("You haven't told me anything yet.")

    elif "joke" in c:
        joke = requests.get("https://v2.jokeapi.dev/joke/Any?type=single").json()
        speak(joke['joke'])

    elif "time" in c:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in c:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "roll a dice" in c:
        dice = random.randint(1, 6)
        speak(f"You rolled a {dice}")

    elif "flip a coin" in c:
        coin = random.choice(["heads", "tails"])
        speak(f"It's {coin}")

    elif "am i lying" in c:
        speak("Tell me something, and I'll judge it.")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            statement = recognizer.recognize_google(audio)
        verdict = random.choice(["You're lying!", "Sounds true to me."])
        speak(verdict)

    elif "creepy mode" in c:
        speak("Entering creepy mode...")
        speak("Did you lock the door? Because... someone's behind you.")

    elif "roast me" in c:
        roasts = [
            "You're like a cloud. When you disappear, it's a beautiful day.",
            "You have something on your chin... no, the third one down.",
            "You're not stupid; you just have bad luck thinking."
        ]
        speak(random.choice(roasts))
    elif "set timer" in c:
        speak("For how many minutes should I set the timer?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                minutes = int(recognizer.recognize_google(audio))
                speak(f"Setting a timer for {minutes} minutes.")
                time.sleep(minutes * 60)
                speak("Time's up!")
            except ValueError:
                speak("I didn't understand that. Please say a number.")
                
    elif "set alarm" in c:
        speak("What time should I set the alarm for? Use 24 hour format like 14:30")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            alarm_time = recognizer.recognize_google(audio)
        speak(f"Alarm set for {alarm_time}")
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == alarm_time:
                speak("Time's up!")
                break
            time.sleep(30)

    else:
        output = aiProcess(c)
        speak_with_mood(output)

if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        try:
            print("Listening for wake word...")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print(f"Detected: {word}")

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("jarvis is listening...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Speech not understood.")
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

