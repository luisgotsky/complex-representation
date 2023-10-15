import cplot as cp
import matplotlib.pyplot as plt
import numpy as np

def f(z): return np.log(z) - np.exp(-z)

xmax = 4.5
ymax = 4.5
n = 1000

plt.figure(figsize=(16, 9))
cp.plot(f, (-xmax,xmax,n), (-ymax,ymax,n))
plt.savefig("cplot.png", dpi=200)
