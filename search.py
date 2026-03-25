import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote

def expand_query(query):
    synonyms = {
        "crowd evacuation": [
            "emergency evacuation",
            "pedestrian evacuation",
            "crowd dynamics evacuation",
            "human evacuation modeling"
        ]
    }

    expanded = [query]

    for key in synonyms:
        if key in query.lower():
            expanded.extend(synonyms[key])

    return list(set(expanded))

import requests

def search_semantic_scholar(query, limit=50):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,url"
    }

    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    
    print("DEBUG STATUS:", response.status_code)
    print("DEBUG RESPONSE:", response.text[:200])

    if response.status_code != 200:
        return []

    data = response.json()
    return data.get("data", [])

def search_papers(query, limit=50):

    print("🔍 Searching Semantic Scholar...")
    semantic_results = search_semantic_scholar(query, limit)

    print("🔍 Searching arXiv...")
    arxiv_results = search_arxiv(query, limit)

    all_results = semantic_results + arxiv_results

    # remove duplicates
    seen = set()
    unique = []

    for paper in all_results:
        title = paper.get("title", "")
        if title not in seen:
            seen.add(title)
            unique.append(paper)

    return unique[:limit]

def search_arxiv(query, limit=50):
    from urllib.parse import quote
    import xml.etree.ElementTree as ET

    query_encoded = quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{query_encoded}&start=0&max_results={limit}"

    response = requests.get(url)

    root = ET.fromstring(response.content)

    papers = []

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()

        authors = [
            author.find("{http://www.w3.org/2005/Atom}name").text
            for author in entry.findall("{http://www.w3.org/2005/Atom}author")
        ]

        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()

        pdf_link = None
        for link in entry.findall("{http://www.w3.org/2005/Atom}link"):
            if link.attrib.get("type") == "application/pdf":
                pdf_link = link.attrib.get("href")

        papers.append({
            "title": title,
            "authors": authors,
            "abstract": summary,
            "pdf": pdf_link
        })

    return papers

