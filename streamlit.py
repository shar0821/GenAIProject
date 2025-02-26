import streamlit as st
import requests
from dotenv import load_dotenv

st.title("Hello World") 

def find_image_type(image) -> str:
    #predict the type of item being captured
    #return the type of item
    #return type
    pass
    return ""
img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if img and st.button("Generate Caption"):
    files={"image":img.getvalue()}
    response=requests.post("http://127.0.0.1:8000/generate_caption",files=files)    

text=st.text_area(response.text)