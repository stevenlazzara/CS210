import sys

if len(sys.argv) != 2:
    print("Usage: python word_count.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        contents = f.read().lower()
        # Split the string at whitespace characters
        words = contents.split()
        # Create a set of unique words
        unique_words = set(words)
        word_count = len(unique_words)
        print(word_count)
except FileNotFoundError:
    print(f"Error: file {filename} not found.")