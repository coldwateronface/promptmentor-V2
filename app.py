# app.py
import streamlit as st
from openai import OpenAI
import os

# Load from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="🧠 PromptMentor 💡 Scanner Builder", layout="centered")

st.title("🧠 PromptMentor 💡 Scanner Builder")
st.markdown("Let me help you build a trading scanner prompt step-by-step.")

query = st.text_input("What do you want to scan for?", placeholder="e.g., RSI breakout with volume confirmation")

if query:
    with st.spinner("Generating your optimized scanner prompt..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert trading strategist. Help the user design a scanner prompt for TradingView or other platforms based on technical signals."},
                    {"role": "user", "content": query}
                ],
                temperature=0.7
            )
            prompt = response.choices[0].message.content
            st.success("✅ Scanner prompt ready!")
            st.code(prompt, language="markdown")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
