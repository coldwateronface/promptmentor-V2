import streamlit as st
import openai
import os

st.set_page_config(page_title="PromptMentor Scanner", layout="centered", initial_sidebar_state="collapsed")
st.title("🧠 PromptMentor 🧠 Scanner Builder")
st.write("Let me help you build a trading scanner prompt step-by-step.")

# Load API Key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1: User Input
user_goal = st.text_input("What do you want to scan for?", placeholder="e.g., EMA crossover + RSI divergence")

if user_goal:
    with st.spinner("Thinking through your strategy..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert trading bot strategist. Help the user break down and expand their scanner idea with clarity."},
                {"role": "user", "content": user_goal}
            ]
        )
        answer = response.choices[0].message.content
        st.subheader("🛠️ Generated Follow-Up Questions or Prompt:")
        st.write(answer)
