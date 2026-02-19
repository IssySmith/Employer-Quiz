"""
This function loads questions from a JSON file and return them indexed by position.
If the file is empty or had whitespace only it is invalid.
Only lists and dictionaries in the file is allowed.
If the file cannot be found an exception is placed to show the user the error.
If the file is found but has invalid JSON, then such error is also displayed.
"""

import json
from typing import Dict, Any

def load_questions(path: str) -> Dict[int, Any]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            raw_data = file.read()
            
            if raw_data.strip() == "":
                print("invalid JSON in questions file")
                return None
                
            data = json.loads(raw_data)  
            
        if isinstance(data,list):
            return {i: q for i, q in enumerate(data)}
        if isinstance(data,dict):
            return data
    
    except FileNotFoundError:
        print("File not found")
        return None
    
    except json.JSONDecodeError:
        print("invalid JSON in questions file")
        return None

    
