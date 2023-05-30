# Frobenious method

# ploting the 2nd order differential equation with variable co-ef

import numpy as np
import matplotlib.pyplot as plt

# Dif eq: y" + xy' + y = 0
# RR: a_n+2 = -a_n / n+2

def ypp(x, y, yp):
    ypp = -x * yp - y         # input differntial equation: y" = ...
    return ypp


xmax = 5                     # increase for more accuracy
# initial conditions
x = 0
y = 0
yp = 1
# step
dx = 0.1

# lists
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)

# Differential Equation, Euler method
while x <= xmax:
    y = y + yp * dx
    yp = yp + ypp(x, y, yp) * dx
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
plt.plot(xpoints, ypoints)

# Power series solution comparison with Euler method
x = 0
xpts = [0]
sum_pts = [0]
n = int(xmax / dx)
terms = 61                     # increase terms for more accuracy
for i in range(1, n + 1):
    x = x + dx
    a = 1
    summ = 0
    for j in range(1, terms, 2):
        summ = summ + a * x ** j
        a = -a / (j + 2)          # input recursion relation
    xpts.append(x)
    sum_pts.append(summ)
plt.plot(xpts, sum_pts)
plt.show()
