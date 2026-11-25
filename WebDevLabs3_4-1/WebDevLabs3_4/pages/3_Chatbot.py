# Lab 3: Chatbot page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

import streamlit as st
from pydantic_ai import Agent
import os
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

agent = Agent(
    "google:gemini-3.5-flash-lite",
    instructions="""You are a friendly assistant for a U.S. cancer statistics and research app.
Help users understand cancer types, public health statistics, and research planning.
Keep answers clear and concise. For unrelated questions, steer the conversation
back to cancer research. Do not provide personal medical advice.""",
)

if "message_history" not in st.session_state:
    st.session_state.message_history = []

if "chat_display" not in st.session_state:
    st.session_state.chat_display = []

for msg in st.session_state.chat_display:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask a question about cancer research...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.chat_display.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Thinking..."):
            result = agent.run_sync(
                prompt,
                message_history=st.session_state.message_history,
            )
        st.session_state.message_history = result.all_messages()
        reply = result.output
    except Exception:
        reply = "Sorry, something went wrong. Please try again in a moment."

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.chat_display.append({"role": "assistant", "content": reply})