import matplotlib.pyplot as mp
from numpy import *
x = 0.0
y = 0.0
xmax = 3.0
dx = 0.01  # step size
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def f(x):
    f = 2 * (exp(-x**2)-x*y)  # derivative of
    return f


while x <= xmax:
    y = y + f(x) * dx
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)

def ff(x):
    ff = 2*x*exp(-x**2)
    return ff

mp.plot(xpoints, ypoints)
x = linspace(0, xmax, 100)
mp.plot(x, ff(x))
mp.show()
