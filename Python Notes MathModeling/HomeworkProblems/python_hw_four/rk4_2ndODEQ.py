# problem 11
# dy2/dx2 + 4y = 0 y(0) = 0,  y'(0) = 1/2
# sol: y = 1/4 sin(2x)
import matplotlib.pyplot as mp
from numpy import linspace
from math import pi, sin


def f(x, y, z):
    f = z
    return f


def g(x, y, z):
    g = -4 * y
    return g


x = 0
y = 0
z = 0.5
dx = 0.3
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)

while x <= 2 * pi:
    k1 = f(x, y, z) * dx
    l1 = g(x, y, z) * dx
    k2 = f(x + dx / 2, y + k1 / 2, z + l1 / 2) * dx
    l2 = g(x + dx / 2, y + k1 / 2, z + l1 / 2) * dx
    k3 = f(x + dx / 2, y + k2 / 2, z + l2 / 2) * dx
    l3 = g(x + dx / 2, y + k2 / 2, z + l2 / 2) * dx
    k4 = f(x + dx, y + k2, z + l2) * dx
    l4 = g(x + dx, y + k2, z + l2) * dx
    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    z = z + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
print(k4, l4)
mp.plot(xpoints, ypoints)


def f(x):
    flist = []
    for i in x:
        f = 0.25 * sin(2*i)
        flist.append(f)
    return flist


x = linspace(0, 2*pi)
mp.plot(x, f(x))
mp.plot([0, 2*pi], [0, 0])
mp.show()
