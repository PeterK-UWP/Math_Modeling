# problem 6
# y'' + y' + y = 2x, y(0) = 0, y'(0) = 2
# ANS:
# y = exp(-x/2)(c1cos(sqrt(3)/2x + c2sin(sqrt(3)/2x))  complimentary
# yp = ax + b:  0 + a + ax +b = 2x: a = 2, b = -2
# y = 2x - 2 particular
# complete:
# exp(-x/2)(c1cos(sqrt(3)/2x + c2sin(sqrt(3)/2x)) + 2x - 2
# using initial conditions we get
# exp(-x/2)((2)cos(sqrt(3)/2x + (2/sqrt3)sin(sqrt(3)/2x)) + 2x - 2

### Euler_2nd_order ###
# solution of y"+2y’+y=0 by Euler method
import matplotlib.pyplot as mp
from numpy import *


# write a function for y''(x)
def ypp(x, y, yp):  # write it generally for x,y,y’
    ypp = 2 * x - y - yp  # differential equation
    return ypp


x = 0
y = 0
yp = 2
dx = 0.1
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)
while x <= 5.0:
    # ytemp=y
    y = y + yp * dx
    yp = yp + ypp(x, y, yp) * dx  #  replace y with ytemp
    # y=y+yp*dx # use this for Euler-Cromer method
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
mp.plot(xpoints, ypoints)


def f(x):
    f = 2 * exp(-x / 2) * (
                cos(sqrt(3)) / 2 * x + (1 / sqrt(3)) * sin(sqrt(3) / 2 * x)) + 2 * x - 2  # analytical solution
    return f


x = linspace(0, 5, 100)
mp.plot(x, f(x))

# ans: it is hard to tell which method is more accurate.
