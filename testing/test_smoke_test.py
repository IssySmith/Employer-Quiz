"""
Runing smoke tests to check the basics of the program works.
Checks that files exist and that they can be imported
"""

from pathlib import Path

def test_app_file_exists():
    assert Path("app.py").exists()

def test_questions_file_exists():
    assert Path("questions.json").exists()

def test_backend_modules_importable():
    from backend import question_loader
    from backend import scoring
    from backend import quiz_engine
    from backend import question_exporter
    assert True

def test_pages_modules_importable():
    from pages import quiz
    from pages import widgets
    assert True

