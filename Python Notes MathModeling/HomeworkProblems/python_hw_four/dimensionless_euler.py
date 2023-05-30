# problem three
# Write differential equation (10) in dimensionless form. Then write a Python program using
# Euler algorithm to solve it numerically in the interval 0 ≤kt ≤5 for T0/Ts = 2, and plot the
# numerical and analytical solutions on the same diagram.

# d(T_ratio)/d(kt) = -(T_ratio - 1), y = ratio, x = kt
# dy/dx = 1 - y

# first-order differential equations by Euler method
"""
import matplotlib.pyplot as mp
from numpy import linspace
from math import *
x = 0.0
y = 2.0
x_max = 5.0
dx = 0.1  # step size
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def T(t):
    T_dimensionless = 1 + (T_ratio - 1) * exp(-kt)
    return T_dimensionless


while kt <= kt_max:
    y = y + T(t) * dx
    kt = kt + dx
    xpoints.append(x)
    ypoints.append(y)
mp.plot(xpoints, ypoints)
x = linspace(0, kt_max, 100)
y = x ** 3  # theoretical graph
mp.plot(x, y)
# ``````````````````
"""
import matplotlib.pyplot as mp
from numpy import *
x = 0.0
y = 2.0  # ratio
dx = 0.1  # step size
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def f(x, y):
    f = 1 - y  # derivative of dy/dx
    return f


while x <= 5:
    y = y + f(x,y) * dx
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)

mp.plot(xpoints, ypoints)
def ff(x):
    ff = 1+exp(-x)
    return ff

x = linspace(0, 5, 100)
mp.plot()
mp.plot(x, ff(x))
mp.show()
