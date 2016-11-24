def check_is_admin(f):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

@check_is_admin
def get_food(*args, **kwargs):
    print('hello')
    pass

get_food('hidoos', 'admin', 'age', username = 'admin')

