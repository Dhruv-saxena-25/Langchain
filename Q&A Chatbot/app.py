# Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv


#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

## Function to load OpenAI model and get respones

def get_openai_response(question):
    llm = OpenAI(model= "davinci-002", temperature= 0.5)
    response = llm(question)
    return response

## Initialize Streamlit APP

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key= "input")
response = get_openai_response(input)

submit = st.button("Ask the Question")

## If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)