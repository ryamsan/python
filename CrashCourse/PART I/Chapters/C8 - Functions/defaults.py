def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')  
# This will make it a default value even if we do not have a parameter inside
describe_pet('willie')
# Python still interprets it as a POSITIONAL arg, matching the order of the parameters.

