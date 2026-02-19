"""
Using pytest to check if the file is loaded correctly.
Uses the correct file, but also a json file that doesn't
exist and one that doesn't have the right format, it's just a string.
"""

from backend.question_loader import load_questions
from pathlib import Path

def test_load_questions_true():
    result = load_questions("questions.json")
    assert result
    assert isinstance(result, dict)
    
def test_load_questions_false():
    assert load_questions("test.json") is None
    assert load_questions("blank.json") is None 