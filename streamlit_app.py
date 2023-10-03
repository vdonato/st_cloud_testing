import streamlit as st

conn = st.connection("snowpark")
st.write(conn)
