


import numpy as np
import matplotlib.pylab as plt

x = np.array([0.2, 0.4, 0.5, 1.5, 3.5], dtype = np.float32)
y = np.array([0.8, 0.7, 0.8, 2.5, 6.0], dtype = np.float32)
y2 = np.array([1, 5 , 6,  8, 9.5], dtype = np.float32)

plt.xlabel("Distancia")
plt.ylabel("Altura")
plt.plot(x, y, "sg")
plt.plot(x, y2,"or")
plt.savefig("grafico.pdf")
plt.show()
