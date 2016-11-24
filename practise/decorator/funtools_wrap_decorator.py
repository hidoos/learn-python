from functools import wraps

def a_new_decorator(a_fun):
    @wraps(a_fun)
    def wrap_decorator_fun():
        print('before fun')
        a_fun()
        print('after fun')

    return wrap_decorator_fun

@a_new_decorator
def login_fun():
    print('login')

login_fun()

print(login_fun.__name__)