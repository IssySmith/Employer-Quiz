class Scoring:
    """
    The class scoring is created to handle the user's points in the quiz engine.
    """
    def __init__(self, score: int):
        """
        Initialises score
        """
        self.score = score
    
    def get_score(self):
        return self.score
    
    def add_point(self) -> int:
        self.score +=1 
        return self.score
    