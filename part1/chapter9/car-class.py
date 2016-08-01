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
# create instace of Car class
my_car = Car('Audi', 'a4', '2015')
my_car.get_full_car_info()
my_car.read_odometer()
my_car.setter_odometer(200)
my_car.read_odometer()
my_car.setter_odometer(180)
my_car.read_odometer()
my_car.increment_odometer(20)
my_car.read_odometer()
