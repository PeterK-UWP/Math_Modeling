# problem 1 (needs to write after every ten steps?) completed
# first-order differential equations by Euler method
import matplotlib.pyplot as mp
from numpy import *
x = 0.0
y = 0.0
xmax = 5.0
dx = 0.2  # step size
xpoints = []
ypoints = []
xpoints.append(x)
ypoints.append(y)


def f(x):
    f = 3 * x ** 2  # derivative of x**3
    return f


while x <= xmax:
    y = y + f(x) * dx
    x = x + dx
    xpoints.append(x)
    ypoints.append(y)
file = open('xy_pairs.txt', 'w')
dataout = column_stack((xpoints, ypoints))
savetxt('xy_pairs.txt', dataout)

mp.plot(xpoints, ypoints)
x = linspace(0, xmax, 100)
y = x ** 3  # theoretical graph
mp.plot(x, y)
mp.show()
"""
date_file('data_out.txt','w')
x = 0
y = 0
dx = 0.01
data_file.write(str(x)+', '+str(y)+'\n')
def f(x):
    f = 3*x**2
    return f
counter = 0
while x<1:
    y = y+f(x)*dx
    x = x+dx
    counter=counter+1
    if counter%10 == 0:
        ...
"""