from car import ElectricCar, Battery

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
my_tesla.battery.get_battery()

# import mutilple class
print('using bettery class')
node_battery = Battery(70)
node_battery.get_battery()
