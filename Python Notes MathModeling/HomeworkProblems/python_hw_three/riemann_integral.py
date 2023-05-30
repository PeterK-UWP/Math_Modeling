# problem 9 complete
# use riemann rectangular integrals
# for number 11 evaluate 1/x with 100 intervals and then 10000

from math import *

n = 100  # n=10000
a = 0
b = 1.
delx = (b - a) / n


def f(x):
    f = x ** 2
    return f


s = 0
for i in range(0, n):
    xi = a + (i + 0.5) * delx
    s = s + f(xi)
integral = s * delx
print(f'integral={integral}')
