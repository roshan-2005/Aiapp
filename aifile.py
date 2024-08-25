import requests
import streamlit as st
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error {response.status_code}: {response.text}")
        return None
        
st.title("Hi Iam Roshan.v.c")
url = "https://www.linkedin.com/in/roshan-v-c-/"

st.markdown(f"LinkedIn Profile")
st.image("linkedin.png")

st.title("AI Image Generator")
st.text("by Roshan")

user_input = st.text_input('Enter your prompt here:')


if st.button('Generate'):
    if user_input:
        image_bytes = query({"inputs": user_input})
        if image_bytes:
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image)
    else:
        st.warning("Please enter a prompt to generate an image.")
