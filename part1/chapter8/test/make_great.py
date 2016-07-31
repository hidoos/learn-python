# 编写一个函数，修改魔术师列表的魔术师名称，每个魔术师前面加 the great 

magicians = ['hidoos', 'rocket child', 'alex young', 'evan you', 'star yeah', 'cult cats']
greet_magicians = []
def make_greet(magicians, greet_magicians):
    while magicians:
        magician = magicians.pop()
        greet_magician = 'the great:' + magician
        greet_magicians.append(greet_magician)

def show_magician(greet_magicians):
    print('\nthe following magicians:')
    for magician in  greet_magicians:
        print('the greet magician:' + magician)

# invoke login function
make_greet(magicians, greet_magicians)
show_magician(greet_magicians)