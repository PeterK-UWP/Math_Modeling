# problem 12
# bessel function
import numpy as np
import matplotlib.pyplot as mp
from scipy.special import *
from numpy import *


def f(x, y, z):
    f = z
    return f


def g(x, y, z):
    g = -z / x - y
    return g

x = 1.0e-100
y = 1.0
z = 0
dx = 0.2
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)

while x<=20:
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
mp.plot(xpoints, ypoints)
x = linspace(0, 20)
mp.plot(x, j0(x))
mp.plot([0, 20], [0, 0])
mp.show()