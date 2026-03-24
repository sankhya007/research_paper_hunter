import pdfplumber
import re

def find_formulas(text):

    formulas = []

    lines = text.split("\n")

    for line in lines:
        if "=" in line and len(line) < 120:
            formulas.append(line.strip())

        # detect math-like patterns
        if re.search(r"[a-zA-Z]\s*=\s*", line):
            formulas.append(line.strip())

    return formulas[:10]

def extract_text(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print("⚠️ PDF read error:", e)
        return ""

    return text


def find_key_sections(text):
    keywords = [
        "method", "model", "approach",
        "result", "experiment",
        "conclusion", "analysis"
    ]

    important = []

    lines = text.split("\n")

    for i, line in enumerate(lines):
        for kw in keywords:
            if kw.lower() in line.lower():
                important.append((i, line))
                break

    return important

def find_formulas(text):

    formulas = []

    lines = text.split("\n")

    for line in lines:
        if "=" in line and len(line) < 120:
            formulas.append(line.strip())

        if re.search(r"[a-zA-Z]\s*=\s*", line):
            formulas.append(line.strip())

    return formulas[:10]