# this program compares the worked out differential equation with the approximated
# equation using the Euler-Richardson method

import matplotlib.pyplot as mp
from numpy import *


def f(x, y, yp):  # write it generally for x,y,y’
    ypp = -(4 * yp + 5 * y)  # differential equation: y"+ 4y'+ 5y = 0
    return ypp


x = 0
y = 0
yp = 1
dx = 0.1
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)
while x <= 3.0:  # interval [0, 3]
    x_mid = x + 0.5*dx
    y_mid = y + yp*.5*dx
    yp_mid = yp + f(x, y, yp) * .5*dx
    ypp_mid = f(x_mid, y_mid, yp_mid)
    y = y + yp_mid * dx
    yp = yp + ypp_mid * dx
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
    mp.plot(xpoints, ypoints)


def f(x):
    f = exp(-2*x)*sin(x)  # analytical solution
    return f


x = linspace(0, 5, 100)
mp.plot(x, f(x))
mp.show()
