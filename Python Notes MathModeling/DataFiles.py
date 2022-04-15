from math import *

# generating data files

# make a list of the functions inputs and outputs
# x: 1,2,3,4,5 ...
# f(x) = x**2

f = open('data.txt', 'w')  # w means writing
i = 1
while i <= 10:
    f.write((str(i)) + ' ' + str(i ** 2) + '\n')
    i = i + 1
f.close()

# read data file
f = open('data.txt')
print('f(x) = x**2')
print(11*'~')
for line in f:
    x, y = line.split()
    x = eval(x)
    y = eval(y)
    print(f'{x:3.0f},{y:4.0f}')

