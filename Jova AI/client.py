import requests
GROQ_API_KEY = "YOUR_GROQ_APIKEY"
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}
command = '''You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud.'''
            

