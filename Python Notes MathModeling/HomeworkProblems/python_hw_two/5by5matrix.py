# problem 7
from numpy import *

matrix = zeros([5, 5], int)
print(matrix)
for i in range(0, 5):
    matrix[i, i] = 1
    print(matrix)

"""   
g = zeros([3, 3], int)
print(g)

g[0, 0] = 1
g[1, 1] = 1
g[2, 2] = 1
print(g)
"""