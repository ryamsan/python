class User:
    
    def __init__(self, first, last, *attributes):
        self.first_name = first
        self.last_name = last
        self.attributes = attributes

    def describe_user(self):
        print(f'{self.first_name}\'s information contains the following:')
        for attribute in self.attributes:
            print(f"- {attribute}")

    def greet_user(self):
        print(f"Greetings, {self.first_name.title()} {self.last_name.title()}!")
        

user1 = User('ryann', 'goh', 'Cool', 'Short')
user1.describe_user()
user1.greet_user()

user2 = User('Ryann', 'Goh', 'Cool', 'Short', 'Gamer')
user2.describe_user()
user2.greet_user()

user3 = User('Ayden', 'Peh', 'Heterosexual')
user3.describe_user()
