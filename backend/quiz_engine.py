from .question_loader import load_questions
from .scoring import Scoring

class Quiz:
    """
    Class to handle quiz functions 
    """
    def __init__(self):
        """
        Initialises the questions, options, and answers
        As well as the number on and score using class imported from scoring
        """
        data = load_questions("questions.json")
        self.questions = list(data.values())
        self.index = 0
        self.score = Scoring(0)

    def another_question(self):
        """
        Checks if there is another question and not at the end of list
        """
        if self.index < len(self.questions):
            return True
        else:
            return False

    def current_question(self):
        """
        Returns the current question, options, index and the length of questions
        """
        if self.index >= len(self.questions):
            return None
        else:
            q = self.questions[self.index]
            return q["question"], q["options"], self.index + 1, len(self.questions)

    def submit_answer(self, answer: int):
        """
        Checks if answer is correct when submitted
        """
        question = self.questions[self.index]
        correct = (answer == question["answer"])
        if correct:
            self.score.add_point()
        self.index += 1
        return correct

    def correct_answer(self):
        """
        Shows what the correct answer is if the user got the answer wrong
        """
        previous = self.index - 1
        if previous < 0:
            return ""
        question = self.questions[previous]
        return question["options"][question["answer"]]

    def final_score(self):
        """
        Returns final score
        """
        return self.score.get_score(), len(self.questions)

