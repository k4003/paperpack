# paperpack

Fetch recent arXiv papers on a chosen topic and summarize them.

## What it does
- `fetch.py` — pulls paper metadata from arXiv and saves it to `papers.json`
- `analyz.py` — reads `papers.json`, ranks the most frequent authors and
  categories, filters papers by a title keyword, and writes a Markdown
  report to `summary.md`

## Setup

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

## Usage

    python fetch.py      # fetch papers -> papers.json
    python analyz.py     # analyze -> prints rankings, writes summary.md

Edit the `QUERY` variable in `fetch.py` to search a different topic,
e.g. `cat:math.NT`.