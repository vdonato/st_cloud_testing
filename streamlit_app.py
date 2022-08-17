import pdfplumber
import streamlit as st

with pdfplumber.open(
    "https://raw.githubusercontent.com/jsvine/pdfplumber/stable/examples/pdfs/background-checks.pdf"
) as pdf:
    img = pdf.pages[0].to_image(resolution=150)
    img.save("./as_image.png", format="PNG")

    st.image("./as_image.png")
