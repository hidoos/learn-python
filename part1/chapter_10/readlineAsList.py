# 按行读取文件，并将文件存到一个列表变量中，再去处理这个列表
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())