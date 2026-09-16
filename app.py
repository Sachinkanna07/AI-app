import os

import google.generativeai as genai
import streamlit as st


st.set_page_config(page_title="Sachin AI Chat", page_icon="🤖")
st.title("Sachin AI Chat")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("GEMINI_API_KEY is not configured. Add it as an environment variable or Streamlit secret.")
    st.stop()

genai.configure(api_key=api_key)

text = st.text_input("Ask a question")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

if st.button("Generate", type="primary"):
    if not text.strip():
        st.warning("Enter a question first.")
    else:
        with st.spinner("Generating response..."):
            response = chat.send_message(text)
        st.write(response.text)
