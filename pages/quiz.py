import streamlit as st
from pages.widgets import hide_toolbar
from backend.question_loader import load_questions
from backend.quiz_engine import Quiz
from backend.scoring import Scoring

hide_toolbar()

st.title("This is the quiz")

questions = load_questions("questions.json")    
session = Quiz()

while session.another_question():
    q, opts, num, total = session.current_question()
    st.markdown(f"Q{num}/{total}: {q}")
    i = 0 
        
    for option in opts:
        i+=1
        st.markdown(f"{str(i)}. {option}")

    answer = int(input("Your answer: ")) - 1
    correct = session.submit_answer(answer)

    if correct:
        st.markdown("Correct!")
            
    else:
        st.markdown("Wrong!")
        st.markdown("The correct answer is:", session.correct_answer())

score, total = session.final_score()
print(f"This is the end, your score is: {score}/{total}")


