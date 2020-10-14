import numpy as np

a = np.array([1, 2])
b = np.array([2, 1])
dot = 0

print(list(zip(a, b)))

for e, f in zip(a, b):
    dot = dot + e * f

print(dot)

print(a * b)

print(np.sum(a * b))
print((a * b).sum())
print(np.dot(a, b))
print(a.dot(b))


amag = np.sqrt((a*a).sum())
print(amag)

amag = np.linalg.norm(a)
print(amag)

cosangle = a.dot(b) / ( np.linalg.norm(a) * np.linalg.norm(b) )
print(cosangle)

angle = np.arccos(cosangle)
print(angle, 'In radians!')
angle_indeg = (angle * 180) / np.pi
print(angle_indeg)