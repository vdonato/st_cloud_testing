import streamlit as st
from time import sleep

st.write("starting")
for i in range(5):
    sleep(1)
    st.write(i)
st.write("finished")
