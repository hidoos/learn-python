filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# brithday is exist pi
brithday = input('\nEnter your brithday')
if brithday in pi_string:
    print('Your brithday appears in the first million digits of pi!')
else:
    print('Your brithday dose not in the first million digits of pi!')