# problem 12 ():
# Write a Python program to read the data file generated in the previous problem and
# plot y versus x, and z versus x on the same diagram.

from numpy import *
import matplotlib.pyplot as plt
f = open('data_trig.txt', 'r')

x, y, z = loadtxt('data_trig.txt', unpack=True)
plt.plot(x, y, z)
