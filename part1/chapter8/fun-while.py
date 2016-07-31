# 

def get_format_fullname(firstname="", lastname=""):
    return firstname.title() + " " + lastname.title()

while True:
    firstname = input("first name:")
    if firstname == 'q':
        break
    lastname = input("last name:")
    if lastname == 'q':
        break
    fullname = get_format_fullname(firstname=firstname,lastname=lastname)
    print("the fullname is:" + fullname)

