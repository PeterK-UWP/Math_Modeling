# this program takes an input as an estimated guess and converges to solve
# for the root of the function.

from math import *

a = eval(input('a:'))  # 0.05 must be greater than 0.
b = eval(input('b:'))  # 0.15
a0 = a
b0 = b
epsilon = 1.0e-8  # input accuracy 8 decimals (e-8)
n = int((log10(b - a) - log10(epsilon)))


def f(x):
    equation = exp(-2 * x) * sin(x) + 2 * exp(x) + log(x)/(x**2 + 1)  # use gnu plot to get good estimation

    return equation


for i in range(1, n + 1):
    xmid = (a + b) / 2
    if f(a) * f(xmid) < 0:
        b = xmid
    elif f(a) * f(xmid) > 0:
        a = xmid
    else:
        print('exact root at', xmid)
print('root=', xmid, ' ', 'accuracy=', epsilon)
print('number of iterations=', n)
