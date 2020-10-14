class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Gas tank is filled now! Drive safe!")


class ElectricCar(Car):  # Name of parent class must be within the parentheses
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialise attributes of the parent Class
        Then initialise attributes specific to an electic car.
        """
        super().__init__(manufacturer, model, year)
        # It is a special func that allows you to call a method from parent class
        # parent == superclass while child == subclass
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the size of battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")  # This overrides the method in parent!


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.read_odometer()  # Method from parent is passed down to child
my_tesla.fill_gas_tank()

my_car = Car('subaru', 'outback', 2019)
my_car.fill_gas_tank()
