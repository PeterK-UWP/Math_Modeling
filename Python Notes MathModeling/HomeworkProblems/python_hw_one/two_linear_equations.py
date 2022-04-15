from math import *
# question 4
# solve the system of 2 linear equations
print('solve 2 linear equations')
a1, b1, c1, = eval(input('a1, b1, c1 :'))
a2, b2, c2, = eval(input('a2, b2, c2 :'))
denominator_determinant = ((a1*b2) - (a2*b1))
if denominator_determinant == 0:
    print('the denominator determinant is zero,')
    print('the functions are not independent of each other')
else:
    x = ((c1*b2) - (c2*b1)) / denominator_determinant
    y = ((a1*c2) - (a2*c1)) / denominator_determinant
    print(f'x is equal to {x}')
    print(f'y is equal to {y}')
