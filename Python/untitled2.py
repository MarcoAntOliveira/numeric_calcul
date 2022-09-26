# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:22:43 2022

@author: miarcos
"""

import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, "o")
plt.grid
plt.show()