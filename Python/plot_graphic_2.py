

import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, "o")
plt.grid
plt.show()
