def a_new_decorator(a_fun):

    def wrap_decorator_fun():
        print('before fun')
        a_fun()
        print('after fun')

    return wrap_decorator_fun

def login_fun():
    print('login')

invoke_fun = a_new_decorator(login_fun)

invoke_fun()