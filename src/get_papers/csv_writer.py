import csv
from typing import List, Dict

def write_csv(filename: str, rows: List[Dict]):
    fieldnames = [
        "PubmedID", "Title", "Publication Date",
        "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
