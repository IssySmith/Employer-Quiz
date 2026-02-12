from .question_loader import load_questions
from .scoring import Scoring

"""
This class does .....
"""

class Quiz:
    def __init__(self):
        data = load_questions("questions.json")
        self.questions = list(data.values())
        self.index = 0
        self.score = Scoring(0)

    def another_question(self):
        if self.index < len(self.questions):
            return True
        else:
            return False

    def current_question(self):
        if self.index >= len(self.questions):
            return None
        else:
            q = self.questions[self.index]
            return q["question"], q["options"], self.index + 1, len(self.questions)

    def submit_answer(self, answer: int):
        question = self.questions[self.index]
        correct = (answer == question["answer"])
        if correct:
            self.score.addpoint()
        self.index += 1
        return correct

    def correct_answer(self) -> str:
        previous = self.index - 1
        if previous < 0:
            return ""
        question = self.questions[previous]
        return question["options"][question["answer"]]

    def final_score(self) -> tuple[int, int]:
        return self.score.get_score(), len(self.questions)


if __name__ == "__main__":
    session = Quiz()

    while session.another_question():
        q, opts, num, total = session.current_question()
        print("")
        print(f"Q{num}/{total}: {q}")
        i = 0 
        
        for option in opts:
            i+=1
            print(f"{str(i)}. {option}")

        answer = int(input("Your answer: ")) - 1
        correct = session.submit_answer(answer)

        if correct:
            print("Correct!")
            
        else:
            print("Wrong!")
            print("The correct answer is:", session.correct_answer())

    score, total = session.final_score()
    print(f"This is the end, your score is: {score}/{total}")
