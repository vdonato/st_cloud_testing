import streamlit as st

conn = st.connection("snowflake")
st.write(conn.query("SELECT 1;"))
