import sys

if len(sys.argv) != 2:
    print("Usage: python word_count.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        contents = f.read()
        word_count = len(contents.split())
        print(word_count)
except FileNotFoundError:
    print(f"Error: file {filename} not found.")
