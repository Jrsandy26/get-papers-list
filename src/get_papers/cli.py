import click
import logging
from get_papers.pubmed_client import search_pubmed, fetch_details
from get_papers.csv_writer import write_csv

@click.command()
@click.argument("query")
@click.option("-f", "--file", type=str, help="Output filename (CSV)")
@click.option("-d", "--debug", is_flag=True, help="Enable debug mode")
def cli(query: str, file: str, debug: bool):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.debug(f"Searching PubMed for query: {query}")
    ids = search_pubmed(query)
    logging.debug(f"Found PubMed IDs: {ids}")

    papers = []
    for pmid in ids:
        try:
            paper = fetch_details(pmid)
            if paper["Non-academic Author(s)"]:
                papers.append(paper)
        except Exception as e:
            logging.warning(f"Failed to process PMID {pmid}: {e}")

    if not papers:
        logging.warning("⚠️ No matching papers found. File created with headers only.")

    if file:
        if isinstance(file, list):
            file = file[0]
        write_csv(file, papers)
        print(f"Results written to {file}")
    else:
        for paper in papers:
            print(paper)
