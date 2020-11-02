import numpy as np

# 1-1
print("1-1")
x = np.array([-3, 2, 8, 9])
k = np.array([0, 1, 2, 3])

ans1 = 3 * np.dot(x, k ** 3) - 3 * np.dot(x, k ** 2) + 5 * np.dot(x, k) + 2
print(ans1)

# 1-2
print("1-2")
x = np.array([-2, 3, 5, 7])
ans2 = np.exp(np.dot(-x, k ** 2))
print(ans2)

# 1-3
print("1-3")
z = np.array([-1 + 2j, 2.3 + 3.5j, -3.7 + 0.1j])
for zi in z:
  rez = zi.real
  imz = zi.imag
  print(np.exp(zi) == np.exp(rez) * (np.cos(imz) + np.sin(imz) * 1j))
