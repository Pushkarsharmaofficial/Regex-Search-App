import re

def search_with_regex(pattern, text):
    
    try:
        matches = re.findall(pattern, text)
        return matches
    except re.error as e:
        return [f"Regex error: {e}"]

def read_file(filepath):
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
