import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("✅ API KEY LOADED:", api_key is not None)
openai.api_key = api_key

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # ✅ Correct way to set API key

# Set mountain background
page_bg = '''
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
'''
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🗻 Chat with AI — Mountain Mode")

# Chat input
user_prompt = st.text_input("You:", placeholder="Say something to the AI...")
submit = st.button("Send")

# Generate response
if submit and user_prompt:
    with st.spinner("AI is thinking..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Always respond in under 100 words."},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            reply = response.choices[0].message.content.strip()

            st.markdown(f'<div class="chat-bubble"><strong>You:</strong> {user_prompt}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-bubble"><strong>AI:</strong> {reply}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
