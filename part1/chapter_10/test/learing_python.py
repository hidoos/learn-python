filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

newsLines = []
for line in lines:
    print(line.rstrip())
    newsLines.append(line.replace('python', 'ruby'))

print('replace python:')
for line in newsLines:
    print(line.rstrip()