"""
Using pytest to check if the Score is set correctly
"""

from backend.scoring import Scoring

def test_score_setup():
    score = Scoring(0)
    assert score.get_score() == 0
    
    score = Scoring(7)
    assert score.get_score() == 7
 
   
def test_addpoint():
    score = Scoring(0)
    assert score.add_point() == 1
    
    
    
    
