import requests
import streamlit as st

st.title(
    "Streamlit gets stuck if session disconnects while waiting for HTTP response, and then tries to reconnect"
)

st.markdown(
    """
<a href="/page2#test" target="_self">page2</a>
""",
    unsafe_allow_html=True,
)

# Button that does something else
if st.button("Another button"):
    st.balloons()

# Button that sends request
if st.button("Send HTTP request"):
    r = requests.post(url="https://httpstat.us/200?sleep=6000")
    st.success("Request completed")
