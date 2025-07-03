import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="EcoHaven Chatbot", page_icon="🌿")
st.title("🌿 EcoHaven Mart Chatbot")
st.write("Ask me anything about EcoHaven Mart!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Your question:", "")
if query:
    response = ask_bot(query)
    st.session_state.chat_history.append(("You", query))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in reversed(st.session_state.chat_history):
    st.write(f"**{sender}:** {message}")