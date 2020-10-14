sandwich_orders = ['abc', 'tuna', 'salmon', 'crabsteak']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f'I am working on your {current_sandwich} sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\n')

for sandwich in finished_sandwiches:
    if sandwich == 'abc':
        print(f'I made an {sandwich} sandwich!')
    else:
        print(f'I made a {sandwich} sandwich!')
