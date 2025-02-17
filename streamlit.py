import streamlit as st

st.title("Hello World") 

def find_image_type(image) -> str:
    #predict the type of item being captured
    #return the type of item
    #return type
    pass
    return ""
img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

def create_caption(type:str,proficiency:str) -> str:
    #create the caption
    #return the caption
    pass    

st.write(img)