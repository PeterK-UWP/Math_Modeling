# problem 1:
# Consider a list a and an array b, each consisting of the ordered set (1,2,3). Write a
# Python program that generates a and b. Then ask the program to print 2a and 2b.
# What is the difference? Also print 2a + 1 and 2b + 1 to see what happens.
from numpy import *

a = [1, 2, 3]
b = array([1, 2, 3], int)
print(a, b)
print(2*a, 2*b)
# c = 2*a + 1 c doesn't work as it is a list, not an array
d = 2*b + 1
print(d)
