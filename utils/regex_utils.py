import re

def search_with_regex(pattern, text):
    """
    Finds all matches of the given regex pattern in the input text.

    Parameters:
        pattern (str): The regex pattern.
        text (str): The text to search.

    Returns:
        list: A list of matched strings.
    """
    try:
        matches = re.findall(pattern, text)
        return matches
    except re.error as e:
        return [f"Regex error: {e}"]

def read_file(filepath):
    """
    Reads text content from a file.

    Parameters:
        filepath (str): Path to the input file.

    Returns:
        str: File contents as a string.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."