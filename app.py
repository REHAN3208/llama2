import requests
import streamlit as st

API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"

st.title("TinyLlama Local Chat")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Your message:")

if st.button("Send") and user_input.strip():
    # Add user message to history
    st.session_state.history.append({"role": "user", "content": user_input})

    # Call Ollama API
    response = requests.post(API_URL, json={
        "model": MODEL_NAME,
        "prompt": user_input
    })

    # Extract text from API response
    if response.status_code == 200:
        reply = response.json().get("response", "").strip()
    else:
        reply = "Error: " + response.text

    # Add model reply to history
    st.session_state.history.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**TinyLlama:** {msg['content']}")
