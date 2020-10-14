import pandas as pd



X = pd.read_csv("data_2d.csv", header=None)



print(type(X))

print(X.info())

print(X.head()) #default is set to 5 rows
try:
    print(X[0,0])
except:
    pass

M = X.values # no longer as_matrix
print(type(M))

print(X[0])

# pandas X[0] -> column with name 0
# numpy X[0] -> 0th row

print(type(X[0]))

print(X.iloc[0])

print(X[[0,2]])

print(X[ X[0] < 5 ])

print(X[0] < 5)
print(type(X[0] < 5))