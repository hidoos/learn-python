user_name = input("what's your name? ")
filename = 'user_name.txt'
with open(filename, 'a') as file_object:
    file_object.write(user_name +'\n')

