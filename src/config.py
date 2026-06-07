import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    import streamlit as st
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

GROQ_MODEL = "llama-3.1-8b-instant"

groq_llm = ChatGroq(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY,
    temperature=0
)