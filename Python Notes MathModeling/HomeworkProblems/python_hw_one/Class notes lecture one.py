from math import *

# this file is used for class notes for homework 5.

# evaluating a + b
print('solving for c = a + b')
a = eval(input('a='))
b = eval(input('b='))
c = a + b
print(f'{"c is equal to"} {c}')

# area of a circle
print('solving for the area of a circle')
while True:
    r = eval(input('r='))
    if r > 0:
        area = pi * r * r
        print(f'{area:0.3f}')
    else:  # enter zero or a negative value, stop the program
        print('done')
    break

# sum n integers simple loop
print('sum the values from 1 to given N value')
N = eval(input('N='))
sum = 0
for i in range(1, N + 1):
    sum = sum + i
print(sum)

# if while loop
x = eval(input('enter x:'))
if x > 0:
    print('x is positive')
elif x == 0:
    print('x is zero')
elif x < 0:
    print('x is negative')
elif x == 1:
    print('x is one')
else:
    print('chicken sandwich')

# quadratic roots
while True:
    a, b, c = eval(input('enter a,b,c:'))
    if a == 0:  # enter zero for a stop program
        print('undefined')
        break
    D2 = b ** 2 - 4 * a * c
    if D2 < 0:
        print('negative square root', D2)
        continue
    D = sqrt(D2)
    negative_root = (-b - D / (2 * a))
    positive_root = (-b + D / (2 * a))
    print('negative root and positive root')
    print(f'{negative_root:0.2f} {positive_root:0.2f}')




