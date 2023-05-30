# problem 5
# relaxation method: provided an x values and a suitable amount of
# iterations, the x value will cycle through the equation until the function converges, this convergence is
# the root of the problem.
# x = e**(-x) + sin(x)  # estimate x with random x
# plot in gnuplot: root btw
from math import *
x = 1.0  # guess
n = 20  # iterations
for i in range(1, n+1):
    x = exp(-x) + sin(x)
    print(x)
