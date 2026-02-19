"""
Streamlit quiz app that shows one question at a time, gives multiple choice options, shows if it was correct or wrong and what the correc
answer was, shows the progress bar, the current score, then the option to move onto the next question.
If the user scores 80% or above then they submit their results to be exported to a csv file
If the user doesn't score high enough, they have to retake the quiz
"""

import streamlit as st
from pages.widgets import hide_toolbar
from backend.quiz_engine import Quiz
from backend.question_exporter import export_to_csv

hide_toolbar()
#st.title(st.session_state['username'], "progress")

if "quiz" not in st.session_state:
    st.session_state.quiz = Quiz()
if "next_question" not in st.session_state:
    st.session_state.next_question = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

quiz = st.session_state.quiz

score, total = quiz.final_score()
completed = getattr(quiz, "index", 0)

progress_fraction = 0 if total == 0 else min(completed, total) / total
st.progress(progress_fraction)
st.caption(f"Progress: {min(completed, total)}/{total}")
st.write(f"Score: {score} / {total}")

if not quiz.another_question() and not st.session_state.next_question:
    st.success(f"Finished! Final score: {score}/{total}")
    if score / total * 100 < 80:
        st.write(f"Sorry you need to pass with over 80%, please try again. You got {int(score/total*100)}%")
        if st.button("Redo"):
            st.session_state.quiz = Quiz()
            st.session_state.next_question = False
            st.session_state.feedback = ""
            st.rerun()
            
    else:
        if st.button("Submit results"):
            export_to_csv("issy", score, total)
            st.success("Submitted!")
            
    st.stop()

if st.session_state.next_question:
    st.info(st.session_state.feedback)
    if quiz.another_question():
        if st.button("Next question"):
            st.session_state.next_question = False
            st.rerun()
    else:
        if st.button("See final score"):
            st.session_state.next_question = False
            st.rerun()
else:
    question, options, number, total = quiz.current_question()
    st.markdown(f"Q{number}/{total}: {question}")

    answer = st.radio("Choose an answer", options)
    submit = st.button("Submit")

    if submit:
        answer_index = options.index(answer)
        is_correct = quiz.submit_answer(answer_index)
        if is_correct:
            st.session_state.feedback = "Correct!"
        else:
            st.session_state.feedback = ("Wrong! The correct answer is: " + quiz.correct_answer())
        st.session_state.next_question = True
        st.rerun()