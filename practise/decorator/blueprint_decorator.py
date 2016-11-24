from functools import wraps

def decorator_name(f):
    @wraps(f)
    def wrap_function(*kargs, **kwargs):
        if not run_fun:
            print('f not run call')
        else:
            print('f can rull call')
            return f(*kargs, **kwargs)

    return wrap_function

@decorator_name
def func():
    print(kargs)
    print(kwargs)
    print('func is running!')
    return("Function is running")

run_fun = False

run_fun = True