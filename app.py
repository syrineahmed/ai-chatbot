import streamlit as st
from chatbot import chat, get_personalities

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("🤖 AI Chatbot")

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    personality = st.selectbox("🎭 Personality", get_personalities())

    if st.button("🗑️ Clear conversation"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.markdown("### 💡 Tips")
    st.markdown("""
    - **HR Assistant** → CV advice, interview prep
    - **Coding Mentor** → Debug code, learn programming  
    - **Career Coach** → Career planning, goals
    - **General** → Any question!
    """)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_personality" not in st.session_state:
    st.session_state.last_personality = personality

if st.session_state.last_personality != personality:
    st.session_state.messages = []
    st.session_state.last_personality = personality

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="message-label" style="text-align:right">You</div>
        <div class="user-message">{message["content"]}</div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message-label">🤖 AI</div>
        <div class="bot-message">{message["content"]}</div>
        """, unsafe_allow_html=True)

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Thinking... 🤔"):
        response = chat(st.session_state.messages, personality)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()