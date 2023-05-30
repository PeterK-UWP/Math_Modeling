
# PROBLEM 4
# this program takes an input as an estimated guess and converges to solve
# for the root of the function.

from math import *

a = eval(input('(I used 0.05) a:'))  # 0.05 must be greater than 0.
b = eval(input('(I Used 0.15)b:'))  # 0.15
a0 = a
b0 = b
epsilon = 1.0e-8  # input accuracy 8 decimals (e-8)
n = int((log10(b - a) - log10(epsilon)))


def f(x):
    equation = exp(-2 * x) * sin(x) + 2 * exp(x) + log(x)/(x**2 + 1)  # use gnu plot to get good estimation

    return equation


for i in range(1, n + 1):
    xmid = (a + b) / 2
    if f(a) * f(xmid) < 0:
        b = xmid
    elif f(a) * f(xmid) > 0:
        a = xmid
    else:
        print('exact root at', xmid)
print('root=', xmid, ' ', 'accuracy=', epsilon)
print('number of iterations=', n)

"""
# PROBLEM 5
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
