import os
import pandas as pd
from search import search_papers
from parser import extract_text, find_formulas, find_key_sections
from analyzer import extract_insights, detect_uniqueness
from scorer import score_paper
from extractor import extract_implementation
from memory import is_new, add_paper
from utils import download_pdf, save_extracted_insights
from parser import find_formulas
from presets import PRESETS
from analyzer import filter_with_context
from utils import list_downloaded_papers


# def run(topic):

#     os.makedirs("output", exist_ok=True)

#     import random

#     start_index = random.randint(0, 50)  # random offset
#     papers = search_papers(topic , limit)

#     print(f"\n🔍 Found {len(papers)} papers\n")

#     results = []

#     for p in papers:

#         print(f"\n📄 Processing: {p['title']}")
#         #import os
#         # safe_title = p["title"][:50].replace("/", "")
#         import re

#         safe_title = re.sub(r'[\\/*?:"<>|]', "", p["title"])
#         safe_title = safe_title.strip()
#         safe_title = safe_title[:50]
        
#         folder = os.path.join("output", safe_title)
#         os.makedirs(folder, exist_ok=True)

#         if os.path.exists(folder):
#             print(f"\n⚠️ Already downloaded: {p['title']}")
#             redownload = input("Redownload? (y/n): ")

#             if redownload.lower() != "y":
#                 continue

#         # TEMP: disable memory (IMPORTANT)
#         # if not is_new(p["id"]):
#         #     continue

#         pdf_path = None

#         if "pdf" in p and p["pdf"]:
#             pdf_path = download_pdf(p["pdf"], f"temp_{len(results)}.pdf")

#         if not pdf_path:
#             print("⚠️ Skipping (no PDF)")
#             continue

#         if not os.path.exists(pdf_path):
#             print("❌ sample.pdf not found")
#             continue

#         text = extract_text(pdf_path)

#         print("📊 Text length:", len(text))

#         if len(text.strip()) == 0:
#             print("⚠️ No text extracted")
#             continue

#         filtered_lines = filter_with_context(text, keywords)

#         filtered_text = "\n".join(filtered_lines)

#         insights = extract_insights(filtered_text)
        
#         print("💡 Insights:", len(insights))

#         unique = detect_uniqueness(insights)

#         score = score_paper(p, insights)

#         implementations = extract_implementation(insights)

#         # save pages
#         #safe_title = "".join(c for c in p['title'] if c.isalnum() or c in " _-")[:30]

#         #folder = os.path.join("output", safe_title)
        
#         import re

#         safe_title = re.sub(r'[\\/*?:"<>|]', "", p['title'])  # remove invalid chars
#         safe_title = safe_title.strip()                      # remove spaces at ends
#         safe_title = safe_title[:30]                         # limit length

#         folder = os.path.join("output", safe_title)

#         # 🔥 VERY IMPORTANT: create folder BEFORE using it
#         os.makedirs(folder, exist_ok=True)

#         formulas = find_formulas(text)

#         save_extracted_insights(
#             folder,
#             insights,
#             formulas,
#             implementations
#         )

#         # add to memory (optional for now)
#         # add_paper(p["id"])

#         results.append({
#             "Title": p["title"],
#             "Authors": ", ".join(p["authors"]),
#             "Score": score,
#             "Unique Idea": unique,
#             "Top Insight": str(insights[:3]),
#             "Formulas": str(formulas[:3]),
#             "Implementation": str(implementations[:2])
#         })

#     if len(results) == 0:
#         print("\n❌ No results generated. Check PDF or extraction.")
#         return

#     df = pd.DataFrame(results)
#     df.to_csv("output/results.csv", index=False)

#     print("\n✅ Done. Results saved.")
    
def display_papers(papers):
    print(f"\nFound {len(papers)} papers:\n")

    for i, p in enumerate(papers):
        title = p.get("title", "No title")
        year = p.get("year", "")
        print(f"[{i}] {title} ({year})")
        
def get_user_selection():
    raw = input("\nEnter paper indices (space separated): ")
    return [int(x) for x in raw.strip().split()]

def process_selected(papers, indices):

    for i in indices:
        if i >= len(papers):
            continue

        p = papers[i]

        print(f"\n📄 Processing: {p['title']}")

        pdf_path = None

        if "pdf" in p and p["pdf"]:
            pdf_path = download_pdf(p["pdf"], f"temp_{i}.pdf")

        if not pdf_path or not os.path.exists(pdf_path):
            print("⚠️ Skipping (no PDF)")
            continue

        text = extract_text(pdf_path)

        print("📊 Text length:", len(text))

        if len(text.strip()) == 0:
            print("⚠️ No text extracted")
            continue

        insights = extract_insights(text)
        print("💡 Insights:", len(insights))

        formulas = find_formulas(text)
        implementations = extract_implementation(insights)

        import re
        #import os

        safe_title = re.sub(r'[\\/*?:"<>|]', "", p['title'])  # remove bad chars
        safe_title = safe_title.strip()                      # remove trailing spaces
        safe_title = safe_title[:50]                         # allow more length

        folder = os.path.join("output", safe_title)
        os.makedirs(folder, exist_ok=True)

        save_extracted_insights(
            folder,
            insights,
            formulas,
            implementations
        )


if __name__ == "__main__":

    print("\n==============================")
    print("📚 RESEARCH PAPER BOT")
    print("==============================\n")

    print("\n1. Search new papers")
    print("2. View downloaded papers")

    choice = input("Choose option: ")
    
    #option 2
    if choice == "2":
            folders = list_downloaded_papers()

            if not folders:
                exit()

            idx = int(input("\nSelect paper to open: "))

            folder = folders[idx]

            print(f"\nOpening: {folder}")
            print(f"Path: output/{folder}")

            exit()
    #option 1
    topic = input("Enter topic: ")
    limit = int(input("How many papers do you want? (e.g. 10, 20, 50): "))
    
    mode = input("Enter mode (panic / hazard / decision / custom): ").lower()

    if mode in PRESETS:
        keywords = PRESETS[mode]
    else:
        raw = input("Enter custom keywords (comma separated): ")
        keywords = [k.strip().lower() for k in raw.split(",")]

    if topic.strip() == "":
        topic = "crowd evacuation"
        
    #topic = topic + " research paper"
    print("\n🚀 Starting...\n")
    
    papers = search_papers(topic , limit)

    display_papers(papers)

    selected_indices = get_user_selection()

    process_selected(papers, selected_indices)

    print("\n✅ Done.")
    
    #run(topic)