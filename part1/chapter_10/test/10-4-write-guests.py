guest_books = 'guest_books.txt'

def input_guest_name():
    print("the follow input your name,thanks!")
    guest_names = []
    while True:
        guest_name = input('input you name: ') 
        guest_names.append(guest_name)
        is_continue = input('is continue? yes/no ')
        if(is_continue == 'no'):
            break
    return guest_names

guest_name_list = input_guest_name()

with open(guest_books, 'a') as file_object:
    for line in guest_name_list:
        file_object.write(line + '\n')