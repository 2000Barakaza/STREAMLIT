
import time  
import random
import numpy as np 
import pandas as pd
import streamlit as st  

# streamed response emulator:
def response_generator():
    response = random.choice([
        " Hey there look at this channels fun Youtube Channel https://youtube.com/shorts/69mtlnMLn3k?si=R-Lfq-LE45LAgxNY"
    ])
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Chatbot")

# Initialize chat history:
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history an app rerun:
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input:
prompt = st.chat_input("What is up?")
if prompt:
    # user typed something, handle it here

    #Add user message to chat history:
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container:
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container:
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

# Add assistant response in chat history:
st.session_state.messages.append({"role":"assistant", "content":"response"})