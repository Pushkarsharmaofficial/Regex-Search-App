import streamlit as st
from utils.regex_utils import search_with_regex, read_file
import os

st.title("🔍 Regex Search Tool")

# Select input method
input_method = st.radio("Choose input method:", ["Paste Text", "Use File"])

# Get input text
text_input = ""

if input_method == "Paste Text":
    text_input = st.text_area("Paste your text here:", height=200)
else:
    # List files in data folder
    files = os.listdir("data")
    selected_file = st.selectbox("Select a file from /data:", files)
    
    if selected_file:
        filepath = os.path.join("data", selected_file)
        text_input = read_file(filepath)
        st.code(text_input[:500], language="text")  # show a preview

# Regex input
pattern = st.text_input("Enter a regex pattern:")

# Search logic
if st.button("Search"):
    if not pattern or not text_input.strip():
        st.warning("Please enter a pattern and text to search.")
    else:
        matches = search_with_regex(pattern, text_input)

        if matches:
            st.success(f"✅ Found {len(matches)} matches:")
            st.write(matches)

            # Save results
            with open("output/results.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(matches))
            st.info("Results saved to `output/results.txt`")
        else:
            st.info("No matches found.")