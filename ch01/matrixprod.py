import numpy as np

A = np.array([[1, 2, 3], [-1, 3, 5]])
B = np.array([[-2, 3], [1, -1], [2, -3]])
u = np.array([1, 2, 5]).reshape(3, 1)

C = np.dot(A, B)
v = np.dot(A, u)
print(C)
print(v)
