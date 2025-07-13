# get-papers-list

**get-papers-list** is a command-line Python tool that fetches PubMed research papers based on a user-specified query and identifies papers authored by individuals affiliated with pharmaceutical or biotech companies.

---

##  Features

-  Search PubMed using any query
-  Identify **non-academic authors** using email/affiliation heuristics
-  Detect affiliations with **biotech/pharma companies**
-  Export results to a CSV file with the following columns:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Author(s)
  - Company Affiliation(s)
  - Corresponding Author Email
-  Output results to CSV or display in console
-  Typed and modular Python code
-  Heuristics to identify company affiliations using keywords
-  Built using Python, [Click](https://click.palletsprojects.com/), and [Poetry](https://python-poetry.org)

---
## Installation

###  Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation) installed

###  Clone the project

```bash

  git clone https://github.com/Jrsandy26/get-papers-list.git

  cd get-papers-list
```
---
Install dependencies

```bash

 poetry install

```
---
 You can run the CLI tool like this:

```bash

poetry run get-papers-list "your search query" -f output.csv --debug
```
---

Example

```bash

poetry run get-papers-list "cancer therapy" -f results.csv --debug

```
---

How Non-Academic Authors Are Identified

Company Affiliation Keywords

```
"pharma", "biotech", "therapeutics", "inc", "ltd", "gmbh", "corp", 
"llc", "company", "technologies", "laboratories", "bio", "genomics"
```
Academic Institution Keywords
```
"university", "college", "institute", "school", "hospital", "center", "centre"
```
Only authors with affiliations that match company keywords but not academic ones are considered non-academic.

---

How It Works

- Uses PubMed API

- Detects non-academic authors using:

- Heuristics: ignores .edu, .ac, university, hospital, institute, etc.

-  Focuses on .com, .org, biotech keywords

- Extracts metadata like title, publication date, authors, and email addresses.

---
## Tech Stack
 
-  Click – CLI framework

-  Requests – HTTP client

-  Poetry – Dependency & packaging

-  Typed Python (mypy support)
---
## Publishing

## To build the package:

```bash

poetry build
```
---
## To publish to Test PyPI:

```bash

poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish -r testpypi
```
- Author
  
   Sandeep Sai Kumar K I
  
   Email: sandeepsai.work@gmail.com
