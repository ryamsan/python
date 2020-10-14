cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars, '\nSorts in alphabetical order! This is permanent.')

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars, '\nThis is sorted in reverse alphabetical order!\n\n--------------\n--------------\n')



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'This is the original list:\n{cars}')
print(f'\nHere is the sorted list (This is not permanent change):\n{sorted(cars)}')
print(f'\nHere is the original list again:\n{cars}')
print(f'\nHere is the sorted list in reverse alphabetical order:\n{sorted(cars, reverse=True)}\n\n--------------\n--------------\n')



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars, '\nThis reverses the original list without arranging in alphabetical order!')

