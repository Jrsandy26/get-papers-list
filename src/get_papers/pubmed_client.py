import requests
from typing import List, Dict

def search_pubmed(query: str) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 50,
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json().get("esearchresult", {}).get("idlist", [])


def fetch_details(ids: List[str]) -> List[Dict]:
    if not ids:
        return []
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "json",
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    summaries = resp.json()["result"]
    return [summaries[i] for i in ids if i in summaries]
