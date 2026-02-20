
"""
This class does .....
"""

from .question_loader import load_questions
from .scoring import Scoring

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
            self.score.add_point()
        self.index += 1
        return correct

    def correct_answer(self):
        previous = self.index - 1
        if previous < 0:
            return ""
        question = self.questions[previous]
        return question["options"][question["answer"]]

    def final_score(self):
        return self.score.get_score(), len(self.questions)

