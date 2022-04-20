# problem 1
# write a program that gets quadratic roots accurately even if ac << b^2 like in eq (3)
from math import *

while True:
    a, b, c = eval(input('enter a,b,c: '))
    if a == 0:  # enter zero for 'a' to stop program
        print('Done')
        break
    D2 = b ** 2 - 4 * a * c
    if D2 < 0:
        print('Negative D')
        continue
    print()
    D = sqrt(D2)
    x1 = (-b - D) / (2 * a)
    x2 = (-b + D) / (2 * a)
    print("x1=", x1, " ", "x2=", x2)

# sol: mult by the conjugate
# x1 = -b - sqrt(b**2 - 4ac) / 2a
# b**2 - (b**2 - 4ac) / 2a(-b -+ sqrt(b**2 - 4ac)
# x2 = 2c / (-b - sqrt(b**2 - 4ac))