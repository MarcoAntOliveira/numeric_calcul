

import numpy as np
import matplotlib.pylab as plt

x , y = np.loadpdf("C:\Users\miarcos\OneDrive\3semestre\Calculo Numérico\Python\naca001034", skiprows  = 1, unpack = true)

x = np.array([0.01, 2.00, -3.10])
np.savetxt("teste.dat", x)

plt.ylim([-0.5, 0.5])
plt.plot(x,y)
plt.show()
