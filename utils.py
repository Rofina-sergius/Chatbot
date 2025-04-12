import requests
import os
from dotenv import load_dotenv
from langdetect import detect

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
}


def get_chat_response(messages, model="deepseek-chat"):
    try:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.7
        }

        response = requests.post(DEEPSEEK_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


def analyze_sentiment(text):
    try:
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"What is the sentiment of this message? "
                        f"Reply only with Positive, Neutral, or Negative:\n{text}"
                    )
                }
            ],
            "temperature": 0.5
        }

        response = requests.post(DEEPSEEK_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Sentiment Error: {e}"


def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"
