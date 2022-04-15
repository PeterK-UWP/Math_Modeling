# problem 4
#                          [row 1 column 1, row 1 column 2
#                           row 2 column 1, row 2 column 2
#                           row 3 column 1, row 3 column 2]
from numpy import *
a = array([[1, 2, -1],
           [0, 1, 3],
           [2, 4, 1]], int)
b = array([[2, 1],
          [1, -1],
          [1, 2]], int)
"""
for blah in something:
    multiply terms a * b 
    add the terms into the matrix term 
    construct the matrix in the format
print(matrix)        
"""
index1_1 = a[0, :] * b[:, 0]
one_one = index1_1[0] + index1_1[1] + index1_1[2]

index1_2 = a[0, :] * b[:, 1]
one_two = index1_2[0] + index1_2[1] + index1_2[2]

index2_1 = a[1, :] * b[:, 0]
two_one = index2_1[0] + index2_1[1] + index2_1[2]

index2_2 = a[1, :] * b[:, 1]
two_two = index2_2[0] + index2_2[1] + index2_2[2]

index3_1 = a[2, :] * b[:, 0]
three_one = index3_1[0] + index3_1[1] + index3_1[2]

index3_2 = a[2, :] * b[:, 1]
three_two = index3_2[0] + index3_2[1] + index3_2[2]

matrix = ([one_one, one_two],
          [two_one, two_two],
          [three_one, three_two])

print(matrix)
