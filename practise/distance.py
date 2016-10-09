import math
def distance(x1, y1, x2, y2):
    x = x2 - x1 
    y = y2 - y1
    dis = x**2 + y**2
    return math.sqrt(dis)

result = distance(1, 2, 4, 6)
print(result)