# problem 5
# print(float(line))
# for line in data:
#     <name of list>.append(line)
from numpy import *
f = open('data_rms.txt', 'w')  # w means writing
i = 1
while i <= 10:
    f.write((str(i)) + ' ' + '\n')
    i = i + 1
f.close()

a = loadtxt('data_rms.txt', int)
print(a)
for i in a:
    a = sum(a)
# print(a)
x_rms = sqrt(a/10)
print(f'the x_rms = {x_rms:0.3f}')
"""
x_array = []
for line in f:
    x_term = line
    x_array = x_term + line

   # x_array.append(x_values)
    print(x_array)
"""

