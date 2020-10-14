pets = []

pet0 = {
    'kind': 'dog',
    'owner\'s name': 'ryan'
}
pets.append(pet0)

pet1 = {
    'kind': 'tortoise',
    'owner\'s name': 'roue'
}
pets.append(pet1)

pet2 = {
    'kind': 'cat',
    'owner\'s name': 'ram'
}
pets.append(pet2)

pet3 = {
    'kind': 'bird',
    'owner\'s name': 'roy'
}
pets.append(pet3)


for pet in pets:
    kind = pet['kind']
    owner = pet['owner\'s name']
    print(f'This {kind.title()} belongs to {owner.title()}.')

