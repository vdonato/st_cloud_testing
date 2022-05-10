import streamlit as st

st.header("Main page content")

st.write(f"logger.level: `{st.get_option('logger.level')}`")
st.write(f"server.baseUrlPath: `{st.get_option('server.baseUrlPath')}`")
