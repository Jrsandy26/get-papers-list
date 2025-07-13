import requests
from bs4 import BeautifulSoup
from get_papers.filters import extract_company_authors_from_xml

def search_pubmed(query: str):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 50}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json().get("esearchresult", {}).get("idlist", [])

def fetch_details(pmid: str) -> dict:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": pmid, "retmode": "xml"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, "lxml-xml")
    article = soup.find("PubmedArticle")
    if not article:
        return {}

    title_tag = article.find("ArticleTitle")
    title = title_tag.text if title_tag else ""

    date_tag = article.find("PubDate")
    pub_date = "-".join([e.text for e in date_tag.find_all()]) if date_tag else ""

    authors = article.find_all("Author")
    non_acads, companies, emails = extract_company_authors_from_xml(authors)

    return {
        "PubmedID": pmid,
        "Title": title,
        "Publication Date": pub_date,
        "Non-academic Author(s)": "; ".join(non_acads),
        "Company Affiliation(s)": "; ".join(companies),
        "Corresponding Author Email": "; ".join(emails),
    }