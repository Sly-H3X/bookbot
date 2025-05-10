def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
# Function above takes "filepath" to a book as input, opens file, and returns the contents as a string
def main():
    return get_book_text("books/frankenstein.txt")
print(main())