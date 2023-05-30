# problem 10 really good method!!! rk4
from numpy import *
import matplotlib.pyplot as mp

x = 0
y = 0
dx = 0.2
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def f(x, y):
    f = 2 * (exp(-x ** 2) - x * y)
    return f


while x <= 3:
    k1 = f(x, y) * dx
    k2 = f(x + 0.5 * dx, y + 0.5 * k1) * dx
    k3 = f(x + 0.5 * dx, y + 0.5 * k2) * dx
    k4 = f(x + dx, y + k3) * dx
    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
mp.plot(xpoints, ypoints)


def ff(x):
    ff = 2 * x * exp(-x ** 2)
    return ff


x = linspace(0, 3)
mp.plot()
mp.plot(x, ff(x))
mp.show()
