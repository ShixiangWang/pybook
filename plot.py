# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()