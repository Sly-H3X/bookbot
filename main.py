from stats import get_word_count
from stats import get_char_count
def main():
    words = get_word_count("books/frankenstein.txt")
    characters = get_char_count("books/frankenstein.txt")
    return f"{words} words found in book", characters
print(main())