# problem 12
# evaluate x**2 e**-x from 0 to inf.
from math import *

n = 100
a = 0
b = 1.0 - 1.0e-16  # set like this as function  is undef at z = 1
h = (b-a) / n


def f(z):
    f = z*exp(-z/(1-z))/(1-z)**3  # transformation
    return f


s = 0.5*f(f(a)+f(b))
for i in range(1, n):
    s = s + f(a+i*h)
integral = s*h
print(f'n={n}')
print(f'integral={integral}')
