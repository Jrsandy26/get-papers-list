# get-papers-list

**get-papers-list** is a command-line Python tool that fetches PubMed research papers based on a user-specified query and identifies papers authored by individuals affiliated with pharmaceutical or biotech companies.

---

##  Features

-  Search PubMed using any query
-  Identify **non-academic authors** using email/affiliation heuristics
-  Detect affiliations with **biotech/pharma companies**
-  Extract corresponding author email addresses
-  Output results to CSV or display in console
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
