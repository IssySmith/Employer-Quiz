"""
The class scoring is created to handle the user's points in the quiz engine.
Losing a point is not an option, you can only get a point or none.
"""

class Scoring:
    def __init__(self, score: int):
        self.score = score
    
    def get_score(self):
        return self.score
    
    def add_point(self) -> int:
        self.score +=1 
        return self.score
    