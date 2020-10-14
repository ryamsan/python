import numpy as np

M = np.array([ [1, 2], [3, 4] ])
L = [ [1, 2], [3, 4] ]

print(L[0])

print(L[0][0], M[0][0])

print(M[0, 0])

M2 = np.array([[1, 2], [3, 4]])

print(M2)

A = np.array([1,2,3])
print(A)
Z = np.zeros(10)
print(Z)
Z = np.zeros((10, 10))
print(Z)

O = np.ones((10, 10))
print(O)

R = np.random.random((10, 10)) # 0<x<1
print(R)

# gaussian distributed numbers?
# G = np.random.randn((10, 10)) ???? Wrong integer required
G = np.random.randn(10, 10)
print(G)

print(G.mean())
print(G.var())