import sys

if len(sys.argv) < 2:
    print("Usage: python sort_words.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Open the file for reading
try:
    with open(filename, 'r') as file:
        words = [line.strip() for line in file.readlines()]
except IOError:
    print(f"Error: Could not open file '{filename}'")
    sys.exit(1)

# Create a list of tuples containing the original word and its lowercase version
lowercase_words = [(word.lower(), word) for line in words for word in line.split()]

# Sort the list of tuples by the lowercase word
lowercase_words.sort()

# Print the sorted words in the original capitalization
for lowercase_word, original_word in lowercase_words:
    print(original_word)
