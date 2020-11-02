import matplotlib.pyplot as plt
import numpy as np

# 1-10
t = np.linspace(-np.pi, np.pi, 1000)
x1 = np.cos(t)
x2 = np.sin(t)

plt.plot(t, x1, linestyle='--')
plt.plot(t, x2)
plt.show()
