import streamlit as st
from pages.widgets import hide_toolbar
from backend.question_loader import load_questions
from backend.quiz_engine import Quiz

hide_toolbar()

st.title("This is the quiz")

questions = load_questions("questions.json")    
session = Quiz()
i = 0

while session.another_question():
    i+=1
    q, opts, num, total = session.current_question()
    st.markdown(f"Q{num}/{total}: {q}")
    
    answer = st.radio("Choose an answer", opts, key = ("Radio" + str(i)))
    
    
    
    
    

