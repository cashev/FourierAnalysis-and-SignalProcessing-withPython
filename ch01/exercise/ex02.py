import numpy as np
import matplotlib.pyplot as plt

# 1-4
t = np.linspace(-5, 5, 1000)
x1 = np.exp(-1 * np.abs(t)) * np.cos(30 * t)
x2 = np.log(1 + t)
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(t, x1)
ax1.set_ylim(-2.5, 2.5)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(t, x2)
ax2.set_ylim(-2.5, 2.5)
plt.show()
