import streamlit as st
import requests

st.title("Sample Streamlit Frontend")

response = requests.get("http://backend:8080/hello")
if response.status_code == 200:
    st.write(response.json())
else:
    st.write("Failed to connect to backend")
