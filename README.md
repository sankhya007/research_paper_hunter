# Research Paper Bot

## Overview

Research Paper Bot is a modular, domain-agnostic research assistant designed to automate the discovery, filtering, and analysis of academic research papers.

The system integrates multiple research sources (Semantic Scholar and arXiv), applies keyword-driven contextual filtering, and extracts structured insights such as methodologies, formulas, and implementation ideas.

It is built to support both targeted research (e.g., crowd evacuation modeling) and general-purpose exploration across multiple domains including artificial intelligence, robotics, healthcare, and systems engineering.

---

## Core Objectives

* Reduce time spent manually reading research papers
* Extract only the most relevant information based on user intent
* Provide structured insights that can be directly implemented
* Enable domain-specific research workflows through presets

---

## Key Capabilities

### 1. Multi-Source Paper Retrieval

* Queries Semantic Scholar API
* Falls back to arXiv for reliable PDF access
* Supports user-defined number of papers

### 2. Interactive Paper Selection

* Displays indexed list of papers
* Allows selective processing instead of bulk analysis

### 3. Keyword-Driven Contextual Filtering

* Extracts only relevant portions of text based on:

  * preset keyword sets
  * custom user-defined keywords
* Includes context window for better understanding

### 4. Domain-Adaptive Preset System

Supports 50+ domains including:

* Crowd dynamics (panic, congestion, hazard)
* Machine learning, deep learning
* Robotics and control systems
* Computer vision and NLP
* Distributed systems and networking
* Mathematics and simulation
* Healthcare and bioinformatics
* Finance and economics

### 5. Insight Extraction Engine

Identifies:

* Models and methodologies
* Algorithms and approaches
* Experimental results
* Implementation-related content

### 6. Formula Detection

* Extracts mathematical expressions and equations
* Useful for simulation and modeling tasks

### 7. Implementation Generator

* Converts insights into:

  * pseudo-code
  * actionable ideas
  * difficulty estimates

### 8. Persistent Storage System

* Saves results per paper in structured folders
* Maintains history of downloaded papers
* Supports re-download control

---

## System Architecture

The system follows a modular pipeline:

User Input → Search → Selection → Extraction → Processing → Output

### Detailed Flow

1. User Input

   * Topic
   * Number of papers
   * Mode (preset or custom keywords)

2. Search Layer

   * Semantic Scholar API
   * arXiv API fallback
   * Deduplication of results

3. Selection Layer

   * Indexed paper display
   * Manual user selection

4. Processing Layer

   * PDF download
   * Text extraction
   * Keyword filtering with context
   * Insight extraction
   * Formula detection
   * Implementation generation

5. Output Layer

   * Structured text files
   * CSV summary

---

## Project Structure

```
research_paper_bot/
│
├── main.py                # Entry point and orchestration
├── search.py              # API integration and paper retrieval
├── parser.py              # PDF parsing and text extraction
├── analyzer.py            # Insight extraction and filtering
├── extractor.py           # Implementation idea generation
├── scorer.py              # Paper scoring logic
├── utils.py               # Utility functions (download, save, history)
├── presets.py             # Keyword preset definitions
├── memory.py              # Processed paper tracking
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── output/                # Generated outputs (ignored in Git)
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sankhya007/research_paper_hunter.git
cd research_paper_hunter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage Guide

Run the program:

```bash
python main.py
```

### Step 1: Select Mode

```
1. Search new papers
2. View downloaded papers
```

---

### Step 2: Enter Inputs

Example:

```
Topic: crowd evacuation
How many papers: 20
Mode: panic
```

---

### Step 3: Select Papers

```
[0] Paper A
[1] Paper B
[2] Paper C
...

Enter indices:
1 2 5
```

---

### Step 4: Processing

For each selected paper:

* PDF is downloaded
* Text is extracted
* Relevant sections are filtered
* Insights and formulas are extracted
* Implementation ideas are generated

---

## Output Format

Each paper generates:

```
output/<paper_name>/
    important.txt
```

### important.txt contains:

* Important insights
* Extracted formulas
* Implementation ideas with pseudo-code

Additionally:

```
output/results.csv
```

Contains a summary of all processed papers.

---

## Keyword Filtering Mechanism

The system filters text using:

* Keyword matching (case-insensitive)
* Context window expansion (±2 lines)

Example:

If keyword = "panic"

Extracted content:

* Lines containing "panic"
* Surrounding context for better understanding

---

## Extending the System

### Adding New Presets

Edit `presets.py`:

```
"your_domain": ["keyword1", "keyword2", ...]
```

---

### Modifying Insight Extraction

Edit `analyzer.py`:

* Add new patterns
* Improve filtering logic

---

### Enhancing Implementation Generator

Edit `extractor.py`:

* Add domain-specific pseudo-code generation
* Improve difficulty estimation

---

## Limitations

* Some papers may not provide downloadable PDFs
* PDF parsing may fail for scanned documents
* Semantic Scholar API may rate-limit requests
* Keyword filtering depends on text quality

---

## Future Improvements

* API retry and caching system
* Insight ranking based on importance
* Keyword highlighting in outputs
* GUI-based interface
* Integration with simulation systems (e.g., TRAGIC)
* Automated mapping of insights to executable models

---

## Use Cases

* Research students extracting key insights quickly
* Simulation developers building models from papers
* AI practitioners exploring new methodologies
* Cross-domain literature analysis

---

## Author

Sankhyapriyo Dey

---

## License

This project is licensed under the MIT License.
