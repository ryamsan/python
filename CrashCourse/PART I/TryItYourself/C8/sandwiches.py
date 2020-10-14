
def items_on_sandwich(*items):
    print("\nThe sandwich has the contents:")
    for item in items:
        print(f"- {item}")
    

items_on_sandwich('mushroom', 'lettuce', 'mayonnaise')
items_on_sandwich('cucumber', 'tomatoes', 'hollandaise')
items_on_sandwich('fish fillet', 'capsicum', 'thousand island')