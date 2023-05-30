# problem 7 second order nonlinear dif eq
# force = -m*g / (1 + y/r)**2
# m = mass
# y = height
# r = earth's radius
# g = 9.81
# set eq. equal to acceleration, cancel mass
# d2y/dx2 = -g / (1 + y/r)**2

### Euler ###
# first-order differential equations by Euler method
import matplotlib.pyplot as mp
from numpy import linspace

g = 9.81
r = 6.37e6


# write a function for y''(x)
def ypp(x, y, yp):  # write it generally for x,y,y’
    ypp = -g / (1 + y / r) ** 2  # differential equation
    return ypp


x = 0
y = 0
yp = 10000  # first derivative is velocity.
dx = 0.1
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)
while x <= 5.0:
    # ytemp=y
    y = y + yp * dx
    yp = yp + ypp(x, y, yp) * dx  # replace y with ytemp
    # y=y+yp*dx # use this for Euler-Cromer method
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
    if y < 0:
        break
mp.plot(xpoints, ypoints)
