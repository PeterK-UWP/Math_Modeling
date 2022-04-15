from math import *

# input function


def f(x_input, y_input):
    function = ((x ** 2) * sin(y)) / 3
    return function


x, y = eval(input('enter x, y: '))
print(f(x, y))
