import click
import logging
from get_papers.pubmed_client import search_pubmed, fetch_details
from get_papers.filters import extract_company_authors, extract_email
from get_papers.csv_writer import write_csv


@click.command()
@click.argument("query")
@click.option("-f", "--file", type=click.Path(), help="Filename to save output CSV.")
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
def cli(query: str, file: str | None, debug: bool) -> None:
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"Searching PubMed for query: {query}")
    ids = search_pubmed(query)

    logging.debug(f"Found PubMed IDs: {ids}")
    papers = fetch_details(ids)

    results = []
    for paper in papers:
        authors = paper.get("authors", [])
        pmid = paper.get("uid", "N/A")
        title = paper.get("title", "No title")
        pubdate = paper.get("pubdate", "Unknown")
        non_acad_authors, companies = extract_company_authors(authors)
        email = extract_email(" ".join(a.get("affiliation", "") for a in authors))

        if non_acad_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pubdate,
                "Non-academicAuthor(s)": "; ".join(non_acad_authors),
                "CompanyAffiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email
            })

    if file:
        write_csv(results, file)
        click.echo(f"Results written to {file}")
    else:
        for row in results:
            click.echo(row)
