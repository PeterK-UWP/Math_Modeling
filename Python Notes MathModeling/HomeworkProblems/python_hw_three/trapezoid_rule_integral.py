# problem 10 complete
# do number 9 but with trapezoial rule
# for number 11 evaluate 1/x with 100 intervals and then 10000

from math import *

n = 10000
a = 0.
b = pi
h = (b - a) / n


def f(x):
    f = x / (1 + sin(x)**2)
    return f


s = 0.5*(f(a) + f(b))
for i in range(1, n):
    s = s+f(a+i*h)
integral = s*h
print(f'n={n}')
print(f'integral={integral}')

