# problem 9
from math import *
# using l = 10, 50, 100
l = 100  # -infinity -> + infinity  this takes a long time 200^3 calculations
M = 0
for i in range(-l, l + 1):
    for j in range(-l, l + 1):
        for k in range(-l, l + 1):
            if i != 0 or j != 0 or k != 0:  # if i**2 + j**2 + k**2 > 0 (!= not equal to)
                M = M + (-1)**(i + j + k) / sqrt(i**2 + j**2 + k**2)
print(M)

# l = 10: -1.69257 ...
# l = 50: -1.73613 ...
# l = 100: -1.74181 ...
