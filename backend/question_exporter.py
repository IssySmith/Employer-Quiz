import csv
from pathlib import Path

def export_to_csv(username: str, score: int, total: int, filepath: str = "quiz_results.csv"):
    percentage = (score / total) * 100
    if percentage >= 80:
        pass_status = "PASS"
    else:
        pass_status = "FAIL"
    
    file_exists = Path(filepath).exists()
    
    with open(filepath, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Username', 'Score', 'Total', 'Percentage', 'Status'])
        writer.writerow([username, score, total, f"{percentage:.1f}%", pass_status])
