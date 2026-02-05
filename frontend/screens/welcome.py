import streamlit as st

st.title("Hello")

user_name = st.text_input("Your name: ")

if user_name:
    st.write(f"hello, {user_name}")


