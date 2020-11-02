import matplotlib.pyplot as plt
import numpy as np

# 1-9
t = np.linspace(-5, 5, 1000)
x1 = np.sin(t)
x2 = np.sin(t**2)
x3 = np.sin(t**2)*np.exp(-t**2/20)
x4 = np.sin(t) ** 3
x5 = np.cos(t)
x6 = np.sqrt(np.abs(t))*np.sin(t)

fig = plt.figure()

ax1 = fig.add_subplot(2, 3, 1)
ax1.plot(t, x1)
ax1.set_ylim(-2.5, 2.5)
ax2 = fig.add_subplot(2, 3, 2)
ax2.plot(t, x2)
ax2.set_ylim(-2.5, 2.5)
ax3 = fig.add_subplot(2, 3, 3)
ax3.plot(t, x3)
ax3.set_ylim(-2.5, 2.5)
ax4 = fig.add_subplot(2, 3, 4)
ax4.plot(t, x4)
ax4.set_ylim(-2.5, 2.5)
ax5 = fig.add_subplot(2, 3, 5)
ax5.plot(t, x5)
ax5.set_ylim(-2.5, 2.5)
ax6 = fig.add_subplot(2, 3, 6)
ax6.plot(t, x6)
ax6.set_ylim(-2.5, 2.5)

plt.show()
