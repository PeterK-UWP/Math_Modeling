import matplotlib.pyplot as mp
from numpy import *
x = 0.0
y = 1.0
xmax = 4.0
dx = 0.2  # step size
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def f(x):
    f = sqrt(y)*exp(-x*y)*log(1+x*y**2)*sin(x-y)**4  # derivative of x**3
    return f


while x <= xmax:
    y = y + f(x) * dx
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)


mp.plot(xpoints, ypoints)
x = linspace(0, xmax, 100)
mp.plot(x, f(x))
mp.show()
