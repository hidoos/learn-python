def count_words(filename):
    """ 统计filename有多少个单词"""
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        messege = "sorry, the file " + filename + 'does not exist'
        print(messege)
    else:
        messege_list = content.split()
        words_count = len(messege_list)
        print('the file ' + filename + ' has about ' + str(words_count) + ' words')

# invoke 
filenames = ['txt/alice.txt', 'txt/little_women.txt', 'txt/siddhartha.txt', 'hello.txt']

for filename in filenames:
    count_words(filename)