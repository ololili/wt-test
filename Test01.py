import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


x = np.linspace(0, 100, num = 5000)
fun = lambda x : np.sin(x**2)**2 * x

y = fun(x)

plt.plot(x, y)

plt.show()
