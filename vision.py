from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load geminipromodel and get responses

model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input != "":
        response=model.generate_content([input, image])
    else:
        response=model.generate_content(image)
    return response.text
## Initialize our Streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

## if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)


