"""
find some words
"""
def find(word, letter, init_index):
    index = 0
    new_word = word[init_index - 1:]
    while index < len(new_word):
        if new_word[index] == letter:
            return index
        index = index + 1
    return -1