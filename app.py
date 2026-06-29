import streamlit as st
from chatbot import chat, get_personalities

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
.user-message {
    background: #e3f2fd;
    border-radius: 15px 15px 0 15px;
    padding: 12px 16px;
    margin: 8px 0;
    margin-left: 20%;
    color: #1565c0;
    font-size: 14px;
}
.bot-message {
    background: #f5f5f5;
    border-radius: 15px 15px 15px 0;
    padding: 12px 16px;
    margin: 8px 0;
    margin-right: 20%;
    color: #333;
    font-size: 14px;
}
.message-label {
    font-size: 11px;
    color: #888;
    margin-bottom: 2px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Chatbot")

#sidebar setting
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

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_personality" not in st.session_state:
    st.session_state.last_personality = personality

# Clear messages when personality changes
if st.session_state.last_personality != personality:
    st.session_state.messages = []
    st.session_state.last_personality = personality
# Display conversation
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

# Input
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