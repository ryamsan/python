def describe_pet(animal_type, pet_name): 
    
    """Display info about a pet"""
    
    print(f'\nI have a {animal_type}.')
    print(f'My {animal_type}\'s name is {pet_name.title()}!')


describe_pet('hamster', 'harry')
describe_pet('dog', 'barry')
describe_pet('barry', 'dog')
# To circumvent this, you can use keyword args which specify, and order is ignored as well!
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

