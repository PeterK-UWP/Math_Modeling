# f(x) = x**2 we want to plot this

from numpy import *
import matplotlib.pyplot as plt
"""
x = linspace(-2, 2, 100)  # from -2 to 2 with 100 intervals
y = x**2*exp(-x)
plt.plot(x, y)
"""
# example makes x, y points in another file
x = linspace(-2, 2, 40)
y = x**2
f = open('plotting.txt', 'w')
dataout = column_stack((x, y))
savetxt('plotting.txt', dataout)
# reading the file and plotting it
f = open('plotting.txt', 'r')
x, y = loadtxt('plotting.txt', unpack=True)
plt.plot(x, y)
