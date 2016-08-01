class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_miles = 0

    def get_full_car_info(self):
        long_name = "The car is: " + self.make + "," + self.model + ',' + self.year
        print(long_name)
        return long_name

    def read_odometer(self):
        print('this car running ' + str(self.odometer_miles) + ' miles')

    def setter_odometer(self, miles):
        if miles > self.odometer_miles:
            self.odometer_miles = miles
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_miles += miles
        print('the car miles incrember ' + str(miles))

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size  = 70

    def get_battery(self):
        print('this car has ' + str(self.battery_size) + '-khw bettery!')

my_tesla = ElectricCar('tesla', 'taxi', '2015')
my_tesla.get_full_car_info()
my_tesla.read_odometer()
my_tesla.setter_odometer(200)
my_tesla.read_odometer()
my_tesla.setter_odometer(130)
my_tesla.read_odometer()
my_tesla.increment_odometer(10)
my_tesla.read_odometer()

# childclass
my_tesla.get_battery()