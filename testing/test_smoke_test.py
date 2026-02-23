from pathlib import Path

def test_app_file_exists():
    """
    Smoke test to check the file exist
    """
    assert Path("app.py").exists()

def test_questions_file_exists():
    """
    Smoke test to check the file exist
    """
    assert Path("questions.json").exists()

def test_backend_modules_importable():
    """
    Smoke test to check the backend files can be imported
    """
    from backend import question_loader
    from backend import scoring
    from backend import quiz_engine
    from backend import question_exporter
    assert True

def test_pages_modules_importable():
    """
    Smoke test to check the pages files can be imported
    """
    from pages import quiz
    from pages import widgets
    assert True

