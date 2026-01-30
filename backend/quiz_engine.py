from question_loader import load_questions
from scoring import Scoring

"""
This python code will use functions from 
"""

def start_quiz():
    questions = load_questions("questions.json")
    if type(questions) is dict:
        score = Scoring(0)
        for num_question, question in questions.items():
            print("")
            print("Q" + str(num_question+1) + ": " + question['question'])
            i = 1
            for option in question["options"]:
                print(str(i) + ". " + option)
                i+=1
            valid = False
            while not valid:
                try:
                    answer = int(input("Your answer: "))
                    valid = True
                except ValueError:
                    print("That wasn't a number :(")
            if answer - 1 == question["answer"]:
                print("Correct!")
                score = score.addpoint()
            else:
                print("Nope! Correct was: " + question['options'][question['answer']])
        print("Game over! You scored " + str(score.get_score) + " / " + str(len(questions)))
    else:
        print(questions)

if __name__ == "__main__":
    start_quiz()
