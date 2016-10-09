def do_n(s = "hello", n = 5):
    if n <= 0:
        return
    else:
        print(s)
        do_n(s = "hello", n = n-1)

do_n()