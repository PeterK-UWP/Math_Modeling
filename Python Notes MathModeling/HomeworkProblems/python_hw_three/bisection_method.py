# problem 4 complete
# bisectional method: interval with one root in [a ,b], f(a)f(b) < 0, x = (a+b)/2
# f(x)f(a) will tell you where the root is left or right of x.
# use a graph of the equation in gnuplot and input rough a and b values to create an interval in
# which the root is guaranteed to be between. provide an accuracy for epsilon and run the code.
from math import *

a = eval(input('a:'))  # 1.5 from the graph 0.8
b = eval(input('b:'))  # 2.7                1.7
a0 = a
b0 = b
epsilon = 1.0e-9  # input accuracy
n = int((log10(b - a) - log10(epsilon)))


def f(x):
    equation = 3*x**7 - 2*x**3 + sin(2*x) + 1  # check gnu plot and we get general points where intercetion ocurrs
    # x ** 2 - 3 * x + 2  : x = 1 and 2
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
