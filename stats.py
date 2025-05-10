def get_word_count(filepath):
    with open(filepath) as f:
        contents = f.read()
    word_list = contents.split()
    count = 0
    for word in word_list:
        count += 1
    return count
# Takes a book's contents and counts each word