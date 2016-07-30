# -*- coding:utf-8 -*-

def get_fullname(firstname='', lastname=''):
    fullname = firstname.title() + lastname.title()
    return fullname

result = get_fullname(firstname="hidoos ", lastname="lan")
print('my fullname is ' + result)
