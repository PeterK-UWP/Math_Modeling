from numpy import *
from math import *

# algebra with arrays
""""
# enumerate for lists
for index, value in enumerate(list):
      new_list[index] = value + 1
"""
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)  # 6, 8, 10, 12
# combined, appended the lists

# arrays not lists
a = array([1, 2, 3, 4], int)
b = array([5, 6, 7, 8], int)
c = a + b
print(c)

# adding 2x2   check!!!
a = array([[1, 2],
           [3, 4]], int)
b = array([[5, 6],
           [7, 8]], int)
c = a + b
print(c)


# grabbing an element
matrix = [[1, 2, 3],  # row 0
          [4, 5, 6],  # row 1 (6 is column 2, so 1, 2)
          [7, 8, 9]   # row 2
          ]
print(matrix[1][2])

# multiplying 1x2 doesn't multiply either with dot or cross product (try [1, 2] * [5, 6]
# dot product: 17
# cross product: determinant
a = array([1, 2], int)
b = array([5, 6], int)
c = cross(a, b)
d = dot(a, b)
print(c, d)  # cross, dot

# multiplying 1x3  [1, 2, 3] * [4, 5, 6]:
# dot: 32
# cross: [-3 6 -3]

# multiplying matrices with different sizes:
# m x p * p x n: columns of one must be equal to the rows of the other
# 2 x 2 * 2 x 3 is allowed [row 1 colum 1, row 1 column 2
#                           row 2 column 1, row 2 column 2]

# nesting do loops will help in very large matrices


# generating array from a file.
# from numpy import loadtxt
a = loadtxt('data.txt', float)
# print(a)

# splicing an array above
b = a[0:2]  # pick out elements 0 to 2-1 ( 0 - 1 )
print(b)  # note it doesn't go to 2, so it will print 0, and 1, and not 2.

# more on the for statement
"""
for i in range(3, n):

for i in range(3, 15, 2):  # from 3 to 15-1 in increments of 2 

the reverse is true (20, 5, -3):  # it will step down in increments of 3
"""

for i in range(1, 7):
    print(i)

for i in [1, 2, 3, 4]:  # print all the values
    print(i)

for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)  # complete nested loop before repeating i
"""
1, 1
1, 2
1, 3
.
.
.
2, 1
2, 2
2, 3
.
.
.
4, 1
4, 2
4, 3
"""

# example:
from math import *
l = 50  # -infinity -> + infinity  this takes a long time 200^3 calculations
M = 0
for i in range(-l, l + 1):
    for j in range(-l, l + 1):
        for k in range(-l, l + 1):
            if i != 0 or j != 0 or k != 0:  # if i**2 + j**2 + k**2 > 0 (!= not equal to)
                M = M + (-1)**(i + j + k) / sqrt(i**2 + j**2 + k**2)
print(M)  # -1.742
