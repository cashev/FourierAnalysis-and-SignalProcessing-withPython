import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
x1 = np.sin(t**2)
x2 = 2*np.sin(t**2)*np.exp(-t**2/20)
x3 = np.sin(t)**3
x4 = np.sqrt(np.abs(t))*np.sin(t)
x5 = np.cos(t)

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(t, x1)
ax1.set_ylim(-2.5, 2.5)

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(t, x2)
ax2.set_ylim(-2.5, 2.5)

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(t, x3)
ax3.set_ylim(-2.5, 2.5)

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(t, x4)
ax4.set_ylim(-2.5, 2.5)

ax3.plot(t, x5)
plt.show()
