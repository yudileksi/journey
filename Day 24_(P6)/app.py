# streamlit run app.py
# It automatically opens your browser at http://localhost:8501

import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# STANDARD FORMULA - page config always first
st.set_page_config(
    page_title="HEELOO BROTHAR",  # CUSTOMIZE
    page_icon="🫡🫡🫡╰(*°▽°*)╯"                 # CUSTOMIZE
)

# STANDARD FORMULA - session state for chat history #This is the most important Streamlit concept for AI apps.
if "messages" not in st.session_state:
    st.session_state.messages = []

# STANDARD FORMULA - display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# STANDARD FORMULA - chat input
user_input = st.chat_input("Type your word man...")  # CUSTOMIZE

if user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        answer = response.choices[0].message.content

    # Add AI response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.write(answer)


