# Research Paper Bot

## Overview

Research Paper Bot is a Python-based system designed to automate the discovery, selection, and analysis of academic research papers. It integrates semantic search techniques with reliable data sources such as Semantic Scholar and arXiv to provide a scalable pipeline for extracting meaningful insights from scientific literature.

The system is built with a human-in-the-loop approach, allowing users to manually select relevant papers before processing, ensuring both precision and control.

---

## Key Features

* Multi-source research paper retrieval (Semantic Scholar + arXiv)
* Query expansion for improved semantic search coverage
* Numbered listing of papers for manual selection
* Selective processing of chosen papers only
* Automated PDF downloading (where available)
* Text extraction from research papers
* Insight extraction based on methodological and experimental keywords
* Formula detection from textual content
* Generation of implementation ideas with pseudo-code
* Structured output storage for further analysis
* CSV export for summarized results

---

## System Workflow

1. User inputs a research topic

2. System performs:

   * Query expansion
   * Semantic Scholar search
   * arXiv fallback search

3. Papers are displayed as a numbered list

4. User selects relevant papers using indices

5. Selected papers are processed:

   * PDF download
   * Text extraction
   * Insight detection
   * Formula extraction
   * Implementation idea generation

6. Results are saved locally for analysis

---

## Example Usage

```bash
python main.py
```

Input:

```
crowd evacuation
```

Output:

```
[0] Paper A
[1] Paper B
[2] Paper C
...
```

Selection:

```
1 2 5 10
```

---

## Project Structure

```
research_paper_bot/
│
├── main.py                # Entry point and workflow control
├── search.py              # Semantic Scholar + arXiv search logic
├── parser.py              # PDF text extraction and parsing
├── analyzer.py            # Insight extraction logic
├── extractor.py           # Implementation idea generation
├── scorer.py              # Paper scoring mechanism
├── utils.py               # Utility functions (download, save)
├── memory.py              # Tracks processed papers
│
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
├── .gitignore             # Ignored files
│
└── output/                # Generated outputs (ignored in git)
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/research-paper-bot.git
cd research-paper-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Output

All processed results are stored in the `output/` directory.

For each paper:

* Extracted insights
* Detected formulas
* Implementation ideas

Additionally:

* `results.csv` containing summarized analysis of all processed papers

---

## Technical Highlights

* Modular architecture for extensibility
* Hybrid search strategy combining semantic and keyword-based retrieval
* Lightweight NLP approach for extracting meaningful insights
* Robust error handling for unreliable PDFs
* Deduplication logic for multi-source aggregation

---

## Limitations

* Some research papers may not include accessible PDF links
* PDF parsing may fail for scanned or non-standard documents
* External APIs may impose rate limits or incomplete responses

---

## Future Work

* Integration with additional academic databases (CrossRef, OpenAlex)
* Advanced ranking and relevance scoring
* Topic-based clustering of research papers
* LaTeX-based formula parsing
* GUI-based interface for improved usability
* Integration with simulation frameworks such as crowd evacuation systems

---

## Author

Sankhyapriyo Dey

---

## License

Licensed under the MIT License
