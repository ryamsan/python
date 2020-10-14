motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles, '\nYou specify the element in which you want to remove!\n\n')



motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_ex = 'ducati'
motorcycles.remove(too_ex)
print(motorcycles)
print(f'A {too_ex.title()} is too expensive for me, hence I am removing it from my favourite bike list')