# notes about errors and stuff

# inverse functions (exp(x) & ln(x) , (sqrt(x))**2 & x)

from math import *

x = 10.
y = exp(log(x))  # (sqrt(x))**2
if x == y:
    print('x and y are equal')
else:
    print('x and y are NOT equal')
    print('x=', x)
    print('y=', y)

# transcendental functions
# x**7 - 5*x - 1 = 0 has at least one root
# for a given root between some interval , [a, b]: like shown in gnuplot
# root 1: [0.0, 0.5], then the function f(x), must have the following relation: f(a)*f(b) < 0 as
# one point must be negative and the other positive.
# check f(a)*f(x1) < 0 if true on left side of x1, and if > 0 root is on the right side of x1
# x1 = (a+b)/2 --> bisection method (Ans: 0.200)

# relaxation method
# write equation as x = g(x)
# x = (x**7 + 1)/5, x=0 --> x = 1/5: x=1/5 --> x=

x = eval(input('x:'))  # guess a value
n = 10  # number of iterations
for i in range(1, n + 1):
    x = f(x)  # type in your equation
    print(x)

# what if you have an equation: x**5 -2x**3 + 1 + x = 0. just add x to both sids and the equation is fixed.
# x = 2*x**2 - exp(-x) --> x - 2*x**2 + exp(-x) = 0 function blows up.
# take derivative of g(x),  and check: |g'(x)| < 1, then the method works,
# sometimes if it fails, the method still works: ex, x**7 - 5*x + 1 --> 7/5 * x**6
# fails the test, but still may or may not work.

# limits
# indeterminate forms: 0/0, inf./inf., 0 * inf., inf. - inf., 1**inf.
# sin(x)/x at x = 0, program on canvas

# 1**inf. code afterwards
# [f(x+delx) - f(x) ] / delx, forward method
# [f(x) - f(x-delx) ] / delx, backward method
# [f(x + delx/2) - f(x - delx/2)] / delx, central method

# [f(x+delx) - 2f(x) + f(x-delx) ] / (delx)^2: derivatives of the definition of the derivative

# Integrals
# Riemann Sum definition works, but is slow converging, using the trapezoidal rule we can converge faster.
# like the averaging in derivative, we average the errors making the error less and more accurate results
# h = (b - a) / n # width, mult by h (33) in notes


# Improper Integrals
# int_{0}^{inf} f(x) dx: make a substitution
# z = x / (1 + x) , solve for x: x = z / (1 - z)  --> dx = dz / (1 - z)**2
# int_{0}^{1} f(z / (1 - z)  dz / (1 - z)**2
# note at z = 1 the integral blows up, but it converges faster than if it was improper
# done in problem 12

## chapter done ##