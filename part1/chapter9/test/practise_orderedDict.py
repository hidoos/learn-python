# -*- coding:utf-8 -*-
"""练习使用python标准库"""

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['Geeh'] = 'python'
favorite_languages['rei'] = 'ruby'
favorite_languages['hidoos'] = 'javascript'

for name, language in favorite_languages.items():
    print(name.title() + "'s favrite language is " +
        language.title() + '.')