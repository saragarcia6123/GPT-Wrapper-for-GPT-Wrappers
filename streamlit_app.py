from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

with open("models.json") as f:
   model_data = json.load(f)

models = [model for model in model_data["models"]]

with open("instructions.json") as f:
    instructions_data = json.load(f)

instructions_list = [line for line in instructions_data['instructions']]
instructions = ' '.join(instructions_list)
print(instructions)

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
