## Image Descriptor
from dotenv import load_dotenv

load_dotenv() #load all environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# configuring API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro vision model and get response
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image):
    #loading the gemini model
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])
    return response.text

st.set_page_config(page_title="Image Descriptor")

st.header("Image Descriptor")
input = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image.")

if submit:
    response = get_gemini_response(input, image)

    st.subheader("The response is:")
    st.write(response)