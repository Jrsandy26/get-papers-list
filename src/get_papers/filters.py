from typing import List, Tuple
import re

COMPANY_KEYWORDS = [
    "pharma", "biotech", "therapeutics", "inc", "ltd", "gmbh", "corp",
    "llc", "company", "technologies", "laboratories", "bio", "genomics"
]

ACADEMIC_KEYWORDS = [
    "university", "college", "institute", "school", "hospital", "center", "centre"
]

def is_company_affiliation(affil: str) -> bool:
    affil_lower = affil.lower()
    return (
        any(kw in affil_lower for kw in COMPANY_KEYWORDS) and
        not any(kw in affil_lower for kw in ACADEMIC_KEYWORDS)
    )

def extract_email(text: str) -> str:
    match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    return match.group(0) if match else ""

def extract_company_authors_from_xml(authors: List) -> Tuple[List[str], List[str], List[str]]:
    non_acads = []
    companies = []
    emails = []

    for author in authors:
        aff_tag = author.find("AffiliationInfo")
        affil = aff_tag.find("Affiliation").text if aff_tag and aff_tag.find("Affiliation") else ""

        lastname_tag = author.find("LastName")
        firstname_tag = author.find("ForeName")

        name = " ".join(filter(None, [
            firstname_tag.text if firstname_tag else "",
            lastname_tag.text if lastname_tag else ""
        ])).strip()

        if affil and is_company_affiliation(affil):
            non_acads.append(name)
            companies.append(affil)
            email = extract_email(affil)
            if email:
                emails.append(email)

    return non_acads, companies, emails

