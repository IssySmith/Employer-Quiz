"""
Using pytest to check if the file is exported correctly.
Checks when the function is ran that the file exists 
"""

from backend.question_exporter import export_to_csv
from pathlib import Path

def test_load_questions():
    export_to_csv("John Doe", 8, 10, "test_quiz_results.csv")
    assert Path("test_quiz_results.csv").exists()
    
