import numpy as np
import matplotlib.pyplot as plt

# 1-7
print("1-7")
def stepfun(t):
  if t >= 1:
    return np.exp(-1 * (t-1) ** 2)
  elif t >= 0:
    return 1
  else:
    return np.cos(10 * t)

t = np.linspace(-2, 5, 1000)
x = np.vectorize(stepfun)
plt.plot(t, x(t))
plt.show()
