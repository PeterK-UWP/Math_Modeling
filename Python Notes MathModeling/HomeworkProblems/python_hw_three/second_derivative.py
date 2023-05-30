# problem 8 complete
# same code as problem 7 just replace for these conditions

# get 2nd derivative of x**2 * sin(x)
# on interval [0, 10pi]


from math import *
from numpy import *
import matplotlib.pyplot as plt

xmin = 0.0
xmax = 10 * pi
dx = 0.1
x = xmin


def f(x):
    f = x**2 * sin(x)
    return f


x_points = []
ypp_points = []
while True:
    ypp = (f(x+dx) - 2*f(x) + f(x-dx)) / dx**2
    x_points.append(x)
    ypp_points.append(ypp)
    x = x + dx
    if x >= xmax:
        break
plt.plot(x_points, ypp_points)


def ff(x):
    ff = (2-x**2)*sin(x) + 4*x*cos(x)
    return ff


x = linspace(xmin, xmax)
plt.plot()
plt.plot(x, ff(x))
plt.show()
