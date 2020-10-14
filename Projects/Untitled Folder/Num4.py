import numpy as np


A = np.array([[1,2], [3,4]])
Ainv = np.linalg.inv(A)

print(Ainv)

print(Ainv.dot(A))
print(A.dot(Ainv))

print(np.linalg.det(A))

print(np.diag(A))

