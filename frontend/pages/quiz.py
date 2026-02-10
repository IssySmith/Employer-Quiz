import streamlit as st
from pages.widgets import hide_toolbar
from ...backend.question_loader import load_questions

hide_toolbar()

st.title("This is the quiz")

questions = load_questions()    

