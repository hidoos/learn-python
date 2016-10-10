list_t = [1,2,3,4]
def bad_del_list(t):
    t = t[1:]
    print('t', t)

bad_del_list(list_t)
print('list_t', list_t)