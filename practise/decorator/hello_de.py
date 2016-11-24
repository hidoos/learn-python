import functools
def logging(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        print("%s called" % func.__name__)
        result = func(*args, **kwargs)
        print("%s end" % func.__name__)
        return result
    return decorator

@logging
def test01(a, b):
    print("in function test01, a=%s, b=%s" % (a, b))
    return 1

@logging
def test02(a, b, c=1, **kwargs):
    print("in function test02, a=%s, b=%s, c=%s" % (a, b, c))
    return 1

print(test01(1, 2))
print(test02(1, 2, c=3, d=4))