import streamlit as st
from pages.widgets import hide_toolbar

hide_toolbar()

st.title("Welcome to IBM's Cyber Security Quiz!")

user_name = st.text_input("Your name: ")

if user_name:
    st.write(f"Hello {user_name}, please press start when you are ready...")

switch_page = st.button("Start")
if switch_page and user_name:
    st.switch_page("pages/quiz.py")