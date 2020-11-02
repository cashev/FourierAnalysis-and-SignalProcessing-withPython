import numpy as np

# 1-5
print("1-5")
C = np.array([[1, 2], [3, 4], [5, 6]])
print(len(C))
print(C.shape[0])
print(C.shape[1])

# 1-6
print("1-6")
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 0], [0, 2], [1, 0]])
print(np.dot(A, B))
