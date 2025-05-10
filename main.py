def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
# Takes "filepath" to a book as input, opens book, and returns the contents as a whole string
def get_word_num():
    text = get_book_text("books/frankenstein.txt")
    word_list = text.split()
    count = 0
    for word in word_list:
        count += 1
    return count
# Puts all separate words in book into list and then counts the number of words in the list
def main():
    return f"{get_word_num()} words found in the document"
print(main())