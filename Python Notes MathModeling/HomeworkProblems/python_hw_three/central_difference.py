# problem 7 complete
# (x + 1)e**(-x)**2
# use central differentialtion method [0, 3]
# f(x) = (x + 1)e**(-x)**2
# f'(x) = e**(-x)**2 + (x + 1)(-2x)e**-x**2
# e**(-x)**2(1 - 2x**2 - 2x)
from math import *
from numpy import *
import matplotlib.pyplot as plt

xmin = 0.0
xmax = 3.0
dx = 0.2
x = xmin


def f(x):
    f = (x + 1) * exp(-x ** 2)
    return f


x_points = []
yp_points = []
while True:
    yp = (f(x + dx / 2) - f(x - dx / 2)) / dx
    x_points.append(x)
    yp_points.append(yp)
    x = x + dx
    if x >= xmax:
        break
plt.plot(x_points, yp_points)


def ff(x):
    ff = (1 - 2 * x - 2 * x ** 2) * exp(-x ** 2)
    return ff


x = linspace(xmin, xmax)
plt.plot()
plt.plot(x, ff(x))
plt.show()
