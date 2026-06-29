# 🤖 AI Chatbot with Memory

An AI-powered chatbot built with Python and Streamlit that remembers conversation history and supports multiple personalities.

## Features
- 🧠 **Conversation memory** — remembers the full chat history
- 🎭 **Multiple personalities** — HR Assistant, Coding Mentor, Career Coach, General Assistant
- 💬 **Clean chat interface** — modern bubble-style messages
- 🗑️ **Clear conversation** — reset anytime from the sidebar

## Built with
- Python
- Groq API (LLaMA 3.3)
- Streamlit
- python-dotenv

## How to run

1. Clone the repo
git clone https://github.com/syrineahmed/ai-chatbot.git

2. Install dependencies
pip install -r requirements.txt

3. Create a `.env` file and add your Groq API key
GROQ_API_KEY=your_key_here

4. Run the app
streamlit run app.py

## Personalities
| Personality | Best for |
|---|---|
| HR Assistant | CV advice, interview prep |
| Coding Mentor | Debug code, learn programming |
| Career Coach | Career planning, goals |
| General Assistant | Any question |

## Author
Syrine Ahmed — [GitHub](https://github.com/syrineahmed)