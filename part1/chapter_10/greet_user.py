import json

filename = "username.json"

def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        print("does't have username")
    else: 
        return username

def save_username(filename):
    """Prompt for a new username."""
    with open(filename, 'a') as f_obj:
        username = input("what's your name?")
        json.dump(username, f_obj)

def greet_user():
    """Greet the user by name."""
    username = get_stored_username(filename)
    if username:
        print('welcome back,'+ username)
    else:
        save_username(filename)

greet_user()


       
    