import streamlit as st

st.set_page_config(page_title="my app wow")

st.header("Main page content")

st.write(f"logger.level: `{st.get_option('logger.level')}`")
st.write(f"server.baseUrlPath: `{st.get_option('server.baseUrlPath')}`")
