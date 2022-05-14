import streamlit as st

st.header("Main page content (for a non-`streamlit_app.py` script)")

st.write(f"logger.level: `{st.get_option('logger.level')}`")
st.write(f"server.baseUrlPath: `{st.get_option('server.baseUrlPath')}`")
