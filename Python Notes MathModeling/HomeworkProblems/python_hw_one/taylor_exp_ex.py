from math import *
# question 7
# approximate e^x given n, and x and output both the taylor expansion and e_n(x) to compare
print('approximating e^x with taylor expansion')
print('more n values make the approximation more precise')
n, x = eval(input('enter n, x:'))
fact = 1
sum = 1
for i in range(1, n):
    fact = fact * i
    # print(factorial_of_n)
    sum = sum + (x**i) / fact
print(f' approximation of e^x with {n} terms is:')
print(f'                  {sum:0.4f}')
e = exp(x)
print(f' e^x is given as: {e:0.4f}')
