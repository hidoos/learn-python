class Record():
    """ this is a record that can record datas """
    a, b, c = 1, 2, ('name', 'hidoos')

r = Record()

r.a = "100"
print r.__dict__
print r.__class__
print r.__doc__ 
print r.__module__  