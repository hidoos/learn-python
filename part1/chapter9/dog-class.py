class Dog():
    def __init__(self, name = 'Naughty', age = 12):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting!')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

my_dog = Dog('Naughty dog')
my_dog.sit()
my_dog.roll_over()