import pandas as pd
import streamlit as st
import numpy as np
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

st.title("Groq Chatbot")

api_key = st.sidebar.text_input("Groq API Key", type="password")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if api_key:

    llm = ChatGroq(model_name ="gemma2-9b-it" , api_key=api_key)

    if prompt := st.chat_input("Ask me anything"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role" :"user" , "content" :prompt})     

        conversation = ""
        for msg in st.session_state.messages:
            conversation += f"{msg['role']}: {msg['content']}\n"


        response = llm.invoke(conversation)  
        content = response.content

        st.chat_message("assistant").markdown(content)
        st.session_state.messages.append({"role" :"assistant" , "content" :response})     
