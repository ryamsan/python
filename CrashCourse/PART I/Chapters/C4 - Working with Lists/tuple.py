dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

try:
    dimensions[1] = 250
except:
    print('No, tuples are immutable')


dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

'''



'''

dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

# Writing over a typle

dimensions = (400, 100)
print('Modified dimensions:')
for dimension in dimensions:
    print(dimension)