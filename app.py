import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load local .env (only works locally)
load_dotenv()

# Get API key from secrets (cloud) or env (local)
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# Optional: Allow user to manually enter key if not found
if not api_key:
    api_key = st.text_input("🔑 Enter your OpenAI API key:", type="password")
    if not api_key:
        st.warning("Please enter an API key to continue.")
        st.stop()

openai.api_key = api_key

# Set mountain background
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1508264165352-258a6c69f207?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    .chat-bubble {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 12px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# UI
st.title("🗻 Chat with AI — Mountain Mode")
user_input = st.text_input("You:", placeholder="Type your message here...")
submit = st.button("Send")

# Handle Chat
if submit and user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Always respond in less than 100 words."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7
            )
            reply = response.choices[0].message.content.strip()

            st.markdown(f'<div class="chat-bubble"><strong>You:</strong> {user_input}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-bubble"><strong>AI:</strong> {reply}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

