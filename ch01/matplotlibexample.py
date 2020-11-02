import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-3, 3, 1000)
plt.plot(t, np.exp(-t**2)*np.sin(20*t))
plt.title('sample grapth $x(t)=e^{-t^2}\sin(20t)$')
plt.xlabel('t')
plt.ylabel('x')
plt.show()
