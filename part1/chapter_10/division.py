print("Give me two numbers, and I'll divide them.\n")
print("Enter 'q' to quit\n")

while True:
    first_number= input('First number:')
    if first_number == 'q':
        break
    last_number= input('Last number:')
    if last_number == 'q':
        break

    try:
        result = int(first_number)/int(last_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:
        print(result)
