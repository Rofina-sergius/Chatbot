import streamlit as st
from utils import get_chat_response

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")

st.title("🤖 TalentScout - Hiring Assistant Chatbot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": (
                "You are an intelligent hiring assistant. "
                "First greet the candidate. Then collect: full name, email, phone, location, years of experience, "
                "desired position, and tech stack. Based on the tech stack, generate 3-5 technical questions for each technology mentioned. "
                "If the user enters 'quit', 'exit', or 'thank you', conclude the conversation politely."
            )
        }
    ]

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": (
            "👋 Hello! I'm TalentScout, your virtual hiring assistant.\n\n"
            "I'll guide you through a quick screening. Let's begin!\n\n"
            "**Please provide the following details:**\n"
            "- Full Name\n"
            "- Email\n"
            "- Phone Number\n"
            "- Location\n"
            "- Years of Experience\n"
            "- Desired Position\n"
            "- Tech Stack (Languages, Frameworks, Tools)"
        )
    })


user_input = st.chat_input("Say something to TalentScout...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = get_chat_response(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

for message in st.session_state.chat_history[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
