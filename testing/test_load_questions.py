from backend.question_loader import load_questions
from pathlib import Path

def test_load_questions_true():
    """
    Using pytest to check if the file is loaded correctly.
    """
    result = load_questions("questions.json")
    assert result
    assert isinstance(result, dict)
    
def test_load_questions_false():
    """
    Using pytest to check if a file is incorrect then its handled correctly
    """
    assert load_questions("test.json") is None
    assert load_questions("blank.json") is None 