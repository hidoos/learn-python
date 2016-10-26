"""
    1: if dict have key , the dict[c] increame 1
"""
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1 
    return d

result = histogram('aaabbbcccddwwaaf')
print(result)