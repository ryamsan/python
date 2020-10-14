sandwich_orders = [
    'pastrami', 'abc', 'tuna', 'pastrami',
    'salmon', 'crabsteak', 'pastrami']

# print(sandwich_orders.count('pastrami'))

finished_sandwiches = []

print('We have run out of pastrami, thus there will be no pastrami sandwiches prepared.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    # print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I am working on your {current_sandwich} sandwich!')
    finished_sandwiches.append(current_sandwich)
    # print(finished_sandwiches)

print('')

for sandwich in finished_sandwiches:
    print(f'I made {sandwich} sandwich for you!')
