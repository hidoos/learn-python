fin = open('words.txt')

def has_no_e(word, letter = 'e'):
    return not word.find(letter) > -1

for line  in fin:
    word = line.strip()
    if len(word) >= 10 and has_no_e(word):
        print(word)
