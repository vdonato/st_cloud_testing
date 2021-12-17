import streamlit as st

if "i" not in st.session_state:
    st.session_state.i = 0


def on_click():
    twenty_million = 320 * 1_000_000
    st.session_state[st.session_state.i] = "A" + (twenty_million * "H")
    st.session_state.i += 1


approximate_memory_usage = len(str(st.session_state)) / 1e6
st.write(f"memory used by session state ~{approximate_memory_usage}MB")

st.button("use more memory!", on_click=on_click)
