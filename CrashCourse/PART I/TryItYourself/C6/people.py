person_0 = {
    'first_name': 'i',
    'last_name': 'am',
    'age': 15,
    'city': 'singapore'
}

person_1 = {
    'first_name': 'not',
    'last_name': 'very',
    'age': 32,
    'city': 'jerusalem'
}

person_2 = {
    'first_name': 'smart',
    'last_name': 'yeet',
    'age': 1532,
    'city': 'newcastle'
}

people = [person_0, person_1, person_2]

for person in people:
    name = f'{person["first_name"].title()} {person["last_name"].title()}'
    age = person['age']
    city = person['city'].title()

    print(f'{name}, of {city}, is {age} years old.')