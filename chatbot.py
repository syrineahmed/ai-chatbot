from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PERSONALITIES = {
    "HR Assistant": "You are an expert HR assistant. You help people improve their CVs, prepare for interviews, and find jobs. You give practical, actionable advice.",
    "Coding Mentor": "You are an expert coding mentor. You help people learn programming, debug code, and improve their skills. You explain things simply with examples.",
    "Career Coach": "You are a professional career coach. You help people plan their careers, set goals, and achieve success. You are motivating and practical.",
    "General Assistant": "You are a helpful, friendly AI assistant. You answer questions clearly and concisely."
}

def chat(messages, personality="HR Assistant"):
    system_prompt = PERSONALITIES[personality]

    full_messages = [
        {"role": "system", "content": system_prompt}
    ] + messages

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=full_messages
    )

    return response.choices[0].message.content

def get_personalities():
    return list(PERSONALITIES.keys())