from ..backend.question_loader import load_questions

def test_load_questions_true():
    assert load_questions("questions.json") == True
    
def test_load_questions_false():
    assert load_questions("test.json") == False
    assert load_questions("blank.json") == False 