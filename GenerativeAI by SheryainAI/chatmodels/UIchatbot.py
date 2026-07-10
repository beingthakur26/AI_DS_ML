from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Mistral AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mistral AI Chatbot")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("AI Mode")

mode_option = st.sidebar.radio(
    "Choose Personality",
    (
        "😡 Angry",
        "😂 Funny",
        "😢 Sad"
    )
)

if mode_option == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif mode_option == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."

else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# -----------------------------
# Model
# -----------------------------
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

# Reset when mode changes
if st.session_state.current_mode != mode:
    st.session_state.current_mode = mode
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# -----------------------------
# Display Chat
# -----------------------------
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.markdown(response.content)

# -----------------------------
# Clear Chat
# -----------------------------
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.rerun()