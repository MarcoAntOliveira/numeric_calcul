
import numpy as np
import matplotlib.pylab as plt

a = 0.1
b = 1.5 
x = (1, 1E-1, 1E-2, 1E-3)
y = np.log2(b - a)/x 

plt.plot(x, y)
plt.show()
