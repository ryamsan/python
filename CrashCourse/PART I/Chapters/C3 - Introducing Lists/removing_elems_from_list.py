motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles, '\nThis is the del method')



motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles, 'This is the pop method! If not specified which index, it will pop the last item')
print(popped_motorcycle)
# How might this be useful???
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(1)
print(f'The last motorcycle I had was a {last_owned.title()}.')