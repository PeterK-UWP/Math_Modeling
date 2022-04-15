# problem 11 ():
# Write a Python program to generate a data file with three columns as follows: The
# first column containing values of x in the range of 0 to 2π in 20 steps and the second and
# third columns the corresponding values of y = sin x and z = cos x, respectively.

from numpy import *
from math import *

x = array(linspace(0, 2 * pi, 20), float)
# print(x)  # gives the array of x values from 0 to 2pi cut into 20 even parts
# f = open('data_trig.txt', 'w')

for i in x:
    x = i
    y = sin(x)
    z = cos(x)
    print(x, y, z)

f = open('data_trig.txt', 'w')
dataout = column_stack((x, y, z))
savetxt('data_trig.txt', dataout)


