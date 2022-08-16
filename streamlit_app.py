import streamlit as st
from wand.image import Image

f = st.file_uploader("upload an image")
if f:
    image_bytes = f.read()
    img = Image(blob=image_bytes)

    flipped = img.clone()
    flipped.rotate(180)
    flipped.save(filename="./flipped.jpg")

    st.image("./flipped.jpg")
