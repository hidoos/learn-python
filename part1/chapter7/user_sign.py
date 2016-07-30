responces = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    responce  = input("which mountain would you like to climb someday?")

    responces[name] = responce

    repeat = input('Would you like to let another person repond? (yes/no)')
    if repeat == 'no':
        polling_active = False

print("\n--- Poll result ---")
for name, responce in responces.items():
    print(name + 'would like to climb ' + responce)
