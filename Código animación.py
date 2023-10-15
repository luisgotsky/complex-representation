import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#Caso de una onda
"""
def f(z, t):
    
    return 3*np.exp(1j*(t+(0.5+0.5j)*z))
"""
"""
#Remolino en el centro

def f(z, t):
    
    return z*np.exp(1j*t)
"""

#Seno con el tiempo

def f(z, t):
    
    return np.sin(z*t)

xmax = 4
ymax = 4
n = 20

x = np.linspace(-xmax, xmax, n)
y = np.linspace(-ymax, ymax, n)
X, Y = np.meshgrid(x, y)
z = X + Y*1j

def plotVector(fig, ax, x, y, u, v):
    
    #Let color be a function of modulus
    
    C = np.hypot(u, v)
    
    #Normalize image arrays

    uNorm = u/C
    vNorm = v/C
    
    ax.cla()
    ax.quiver(x, y, uNorm, vNorm, C)
    
tmax = 3
frames = 100

t = np.linspace(0, tmax, frames)

def updateAnim(t):
    
    global ax, fig, z, X, Y, f
    
    u = np.real(f(z, t))
    v = np.imag(f(z, t))
    
    plotVector(fig, ax, X, Y, u, v)

fig, ax = plt.subplots()

anim = FuncAnimation(fig, updateAnim, frames=t, interval=0.1)
anim.save("Seno.gif", dpi=200)