# app.py
import streamlit as st
from openai import OpenAI
import os

# --- Set up Streamlit page ---
st.set_page_config(page_title="🧠 PromptMentor Scanner Builder", page_icon="🧠")
st.title("🧠 PromptMentor  💡 Scanner Builder")
st.write("Let me help you build a trading scanner prompt step-by-step.")

# --- Load API Key ---
client = OpenAI()

# --- Step 1: Get user input ---
user_input = st.text_input("What do you want to scan for?")

# --- Step 2: Generate prompt using GPT-4 ---
if user_input:
    try:
        with st.spinner("Generating your scanner prompt..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a professional trading assistant who helps build technical scanner prompts."},
                    {"role": "user", "content": f"Build a TradingView scanner prompt for: {user_input}"}
                ]
            )

            output = response.choices[0].message.content
            st.subheader("📤 Scanner Prompt")
            st.code(output, language="markdown")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
