def get_word_count(filepath):
    with open(filepath) as f:
        contents = f.read()
    word_list = contents.split()
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count
# Takes a book's contents and counts each word
def get_char_count(filepath):
    with open(filepath) as f:
        contents = f.read()
    word_list = contents.split()
    char_list = []
    char_count = {}
    for word in word_list:
        for char in word:
            low_char = char.lower()
            char_list.append(f"{low_char}")
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
# Takes a book's contents and then counts how many times a character is used in the book