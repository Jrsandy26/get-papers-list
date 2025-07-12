from typing import List, Tuple
import re

def extract_company_authors(authors: List[dict]) -> Tuple[List[str], List[str]]:
    non_academic = []
    companies = []
    for author in authors:
        affil = author.get("affiliation", "")
        name = author.get("name", "")

        if affil and not re.search(r"university|college|institute|school|hospital", affil, re.IGNORECASE):
            non_academic.append(name)
            companies.append(affil)

    return non_academic, companies

def extract_email(text: str) -> str:
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else ""
