from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

instructions="You are a specialist vibe coder in creating ChatGPT Wrappers. Always stay on topic."

client = OpenAI(api_key=OPENAI_API_KEY)

with open("models.json") as f:
   data = json.load(f)

models = [model for model in data["models"]]

import streamlit as st

model = st.selectbox(label="Select a model", options=models)

message = st.text_input(label="Message", placeholder="How to make a ChatGPT wrapper")

if st.button("Send"):
    response = client.responses.create(
      model=model,
      instructions=instructions,
      input=message,
    )
    st.write(response.output_text);
