# arbitrary number of arguments may be encountered


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza2(*toppings):
    """Summarise the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza2('pepperoni')
# make_pizza2('mushrooms', 'green peppers', 'extra cheese')


def make_pizza3(size, *toppings):
    """Summarize the pizza we are about to make. This mixes positional and arbitrary args"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza3(16, 'pepperoni')
# make_pizza3(12, 'mushrooms', 'green peppers', 'extra cheese')
