import streamlit as st
from pages.widgets import hide_toolbar

hide_toolbar()
base = "light"

st.title("Welcome to IBM's Cyber Security Quiz!")

user_name = st.text_input("Your name: ")

if user_name:
    st.write(f"Hello {user_name}, please press start when you are ready...")

# Button to switch page
switch_page = st.button("Switch page")
if switch_page:
    st.switch_page("pages/quiz.py")