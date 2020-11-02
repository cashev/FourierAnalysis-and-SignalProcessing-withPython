import numpy as np

def stepfun(t):
  if t >= 5:
    return 1
  elif t >= 0:
    return 0
  else:
    return -1

npstepfun = np.vectorize(stepfun)

t = np.linspace(-5, 10, 16)
print(npstepfun(t))
