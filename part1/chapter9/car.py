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
        self.battery = Battery(70)

    def get_battery(self):
        print('this car has ' + str(self.battery_size) + '-khw bettery!')

class Battery():
    def __init__(self, battery_size):
        self.battery_size = 70

    def get_battery(self):
        print('this car has ' + str(self.battery_size) + '-khw bettery!')