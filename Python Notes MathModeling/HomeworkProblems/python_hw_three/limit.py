# problem 6 compete
# calculate the limit
# lim as n to inf. cos(pi/(2n))**(2n) show be 1
# define x = 2n
# y = cos(pi/x)**x # ln of both sides
# lny = xln(cos(pi/x)) # take the limit now.
# lny = inf.ln(cos(0)) = inf.*0
# lim  lncos(pi/x) / 1/x = LH = -sin(pi/x)(-1/x**2)/cos(pi/x) (-1/x**2)
# -sin(pi/x) / cos(pi/x) = -tan(pi/x) as x --> inf. tan(0) = 0
# lny = 0 --> y = e**0 = 1. :)

from math import *


def f(n):
    f = (cos(pi / n)) ** n
    return f


while True:
    n = eval(input('n='))
    if n < 0:
        break
    print(f'f(n)={f(n)}')
