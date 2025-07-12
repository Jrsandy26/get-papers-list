import csv
from typing import List, Dict

def write_csv(data: List[Dict], filename: str) -> None:
    if not data:
        return

    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
