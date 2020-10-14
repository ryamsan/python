requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print('''
--------------
''')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('\nFinished making your pizza!')


print('''
--------------
''')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:

    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now!')
    else:
        print(f'Adding {requested_topping}')

print('\nFinished making your pizza!')


print('''
--------------
''')


requested_toppings = []

if requested_toppings: # An empty list evaluates to False
    for requested_topping in requested_toppings:
        print(f'Adding {requested_toppinge}')
    print('\nFinished making your pizza!')

else:
    print('Are you sure you want a plain pizza?')
