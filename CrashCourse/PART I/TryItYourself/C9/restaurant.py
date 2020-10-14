class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.resturant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.resturant_name}, and it serves {self.cuisine_type} cuisines")

    def open_restaurant(self):
        print(f"The {self.resturant_name} restaurant is open for business!")


# This is one instance of the Restaurant class
restaurant = Restaurant('Aldini Ribeye Steak', 'Italian')

restaurant.describe_restaurant()
restaurant.open_restaurant()
