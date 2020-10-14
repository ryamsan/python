# """A class that can be used to represent a car."""
"""A set of classes used to represent gas and electric cars."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialise attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Assign a default value

    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """
        # This adds logic to make sure no one rolls back the meter
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        # This allows us to add increments and not set a new value all the time
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        # if self.battery_size == 75:
        #     range = 260
        # elif self.battery_size == 100:
        #     range = 315
        range = self.battery_size * 3.13424
        print(f"This car can go about {int(range)}  miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


# Originally only with Car class. Now this has become a module.
'''
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attribute values directly!
my_new_car.odometer_reading = 5
my_new_car.read_odometer()

# Use a method instead to change your attribute values
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(22)
my_new_car.read_odometer()  # Still the same mileage!

print('\n')

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# Uses increments to change the attribute value
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
'''