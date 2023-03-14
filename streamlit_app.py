import streamlit as st

st.write(st.secrets.foo)
st.write(st.secrets.bar)
st.write(st.secrets.baz.qux)
st.write(st.secrets.nonexistent)
