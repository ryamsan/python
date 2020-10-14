class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.resturant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.resturant_name}, and it serves {self.cuisine_type} cuisines")

    def open_restaurant(self):
        print(f"The {self.resturant_name} restaurant is open for business!")


restaurant1 = Restaurant("McDonald's", 'Fast Food')
restaurant2 = Restaurant("Mizuhara Tastes", 'Japanese')
restaurant3 = Restaurant("Ma La Xiang Guo", 'Chinese')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
