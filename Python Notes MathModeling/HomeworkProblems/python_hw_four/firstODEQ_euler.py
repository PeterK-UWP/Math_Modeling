# problem four and five
# dy/dx = 2(e^-x^2) - xy), y(0) = 0
# dy/dx = 2(e^-x^2) - 2xy, y(0) = 0
# dy/dx + 2xy = 2exp(-x^2)

# get integrating factor: I = exp(int(p(x)dx))
# I = exp(2intxdx) = exp(x^2)
# mult both sides by I to simplify

# exp(x^2)dy/dx + 2xexp(x^2)y = 2
# note the eft hand side is just: d/dx(yexp(x^2))

# d/dx(yexp(x^2)) = 2  --> dyexp(x^2) = 2dx
# yexp(x^2) = 2x + C
# y = (2x + C) exp(-x^2), y(0) = 0
# 0 = 0 + C, C = 0
# y = 2x * exp(-x^2)

import matplotlib.pyplot as mp
from numpy import *
x = 0.0
y = 0.0
xmax = 3.0
dx = 0.2  # step size
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def f(x):
    f = 2 * (exp(-x**2)-x*y)  # derivative of x**3
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

# number 5
# y = 1
# dx = 0.001
# f = crazy function
# xmax =4
# no need for ff(x)
