import numpy as np

print('Hello world!')

L = [1, 2, 3]
A = np.array([1, 2, 3])

for e in L: #lists are way slower than numpy arrays
    print(e)

for e in A:
    print(e)

L.append(4)

print(L)

try:
    A.append(4)
    print(A)
except:
    print('No such thing as append on a numpy array')

L = L + [5]
print(L)

try:
    A = A + [4, 5]
    print(A)
except:
    print('Cant add')


L2 = []
for e in L:
    L2.append(e + e)
print(L2)

print(A + A) # vector addition

print(2*A)
print(2*L)

for e in list(range(1,6)):
    print(e*e)

L2 = []
for e in list(range(1,6)):
    L2.append(e*e)
print(L2)

print(A**2)



print(A)
print(np.sqrt(A))
print(np.log(A))
print(np.exp(A))


'''
There are many types of numpy Arrays

with different dimensions

0-D , 1-D, 2-D, 3-D, etc...
'''

A0 = np.array(42)
print(A0)
A1 = np.array([1,2,3,4,5])
print(A1)
A2 = np.array([[1,2,3],[4,5,6]])
print(A2)

print(A0.ndim)
print(A2.ndim)
