# problem 8

# ypp = -(2 * yp + y)
### Euler_2nd_order ###
# solution of y"+2y’+y=0 by Euler method
import matplotlib.pyplot as mp
from numpy import *


def f(x, y, yp):  # write it generally for x,y,y’
    ypp = -(2 * yp + y)  # differential equation
    return ypp


x = 0
y = 0
yp = 1
dx = 0.1
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)
while x <= 5.0:
    x_mid = x + 0.5*dx
    y_mid = y + yp*.5*dx
    yp_mid = yp + f(x, y, yp) * .5*dx
    ypp_mid = f(x_mid, y_mid, yp_mid)
    y = y + yp_mid * dx
    yp = yp + ypp_mid * dx
    # y=y+yp*dx # use this for Euler-Cromer method
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
    mp.plot(xpoints, ypoints)


def f(x):
    f = x * exp(-x)  # analytical solution
    return f


x = linspace(0, 5, 100)
mp.plot(x, f(x))
