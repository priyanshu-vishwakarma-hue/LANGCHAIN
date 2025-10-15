import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama   # or from langchain_ollama import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser    # do chatgpt for this if not understand 

load_dotenv()
## Langsmith Tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING_V2"]="true"
os.environ["LANGSMITH_ENDPOINT"]=os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")


## prompt template

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistence, please respond to the question asked"),
    ("user","question:{question}")
])


## Steamlit model

st.title("Langchain Demo model with phi4-mini:latest")
input_text=st.text_input("what question you have in mind? ")


## Ollama phi4-mini:latest model

llm=Ollama(model="phi4-mini:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    