class Car:

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


class Battery:  # New class that doesn't inherit from any other class
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        # if self.battery_size == 75:
        #     range = 260
        # elif self.battery_size == 100:
        #     range = 315
        range = self.battery_size*3.13424

        print(f"This car can go about {int(range)} miles on a full charge.")


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):

        super().__init__(manufacturer, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


your_tesla = ElectricCar('tesla', 'model x', 2020)
your_tesla.battery = Battery(100)

print(your_tesla.get_descriptive_name())
your_tesla.battery.describe_battery()
your_tesla.battery.get_range()
