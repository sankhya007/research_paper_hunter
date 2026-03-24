import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return set()
    with open(MEMORY_FILE, "r") as f:
        return set(json.load(f))

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(list(memory), f)

def is_new(paper_id):
    memory = load_memory()
    return paper_id not in memory

def add_paper(paper_id):
    memory = load_memory()
    memory.add(paper_id)
    save_memory(memory)