import json
from typing import Dict, Any

"""
This function loads questions from a JSON file and return them indexed by position.
If the file cannot be found an exception is placed to show the user the error.
If the file is found but has invalid JSON, then such error is also displayed.
"""

def load_questions(path: str) -> Dict[int, Any]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print("Worked")
        return {i: q for i, q in enumerate(data)}
    
    except FileNotFoundError:
        print("File not found")
    
    except json.JSONDecodeError:
        print("invalid JSON in questions file")

    
