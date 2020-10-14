# from car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = Car('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

import car  # Use dot notation to prevent naming conflicts

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.Car('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
