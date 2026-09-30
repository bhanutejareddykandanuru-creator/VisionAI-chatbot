from distutils.command.config import config
from gtts import gTTS
import io
def speak(text):
    mp3 = io.BytesIO()
    gTTS(text=text, lang='en').write_to_fp(mp3)
    mp3.seek(0)
    return mp3

import streamlit as st
from backend import chatbot_graph
from langchain_core.messages import HumanMessage
st.set_page_config(page_title="Vision AI", page_icon="🦅")
st.header("Vision AI🦅")

with st.chat_message('assistant'):
    st.markdown('ai_message')
    st.audio(speak('ai_message'), format="audio/mp3")

with st.sidebar:
    st.title("🦅 Vision AI")
    st.caption("Your smart AI assistant")
    st.button("➕ New Chat")

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Enter your message")

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot_graph.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    with st.spinner("Thinking..."):
        response = chatbot_graph.invoke(
            {'messages': [HumanMessage(content=user_input)]}, config=CONFIG
        )
    ai_message = response['messages'][-1].content

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)