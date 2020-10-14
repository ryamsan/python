# cubes = []
# for num in range(1, 11):
#     cubes.append(num**3)
#
# print(cubes)
#
# for cube in cubes:
#     print(cube)

cubes = [num**3 for num in range(1, 11)]
print(cubes)

for cube in cubes:
    print(cube)