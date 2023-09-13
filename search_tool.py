import streamlit as st
import os

def search_filenames(term, root_dir=os.path.expanduser("~")):

    """Search filenames for the term."""
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if term.lower() in filename.lower():
                matches.append(os.path.join(root, filename))
    return matches
def search_file_content(term, root_dir=os.path.expanduser("~")):
    """Search inside files for the term."""
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.exists(file_path):  # Check if the file exists before opening
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        if term.lower() in f.read().lower():
                            matches.append(file_path)
                except Exception as e:  # Catch any other unexpected errors while reading
                    print(f"Error reading {file_path}: {e}")
    return matches

# Streamlit UI
st.title("File Search Tool")

term = st.text_input("Enter the word or sequence of words to search:")
search_type = st.radio("Where do you want to search?", ("In Filenames", "Inside File Content"))

if st.button("Search"):
    if search_type == "In Filenames":
        results = search_filenames(term)
    else:
        results = search_file_content(term)

    st.write("Results:")
    for r in results:
        st.write(r)

if __name__ == "__main__":
    pass
