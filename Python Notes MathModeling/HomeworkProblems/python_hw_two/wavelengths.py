# problem 10
from numpy import *

R = 0.0109678  # nm
n1 = array([1, 2, 3], int)
"""
n2 = array([2, 3, 4],
           [3, 4, 5],
           [4, 5, 6], int)
"""
for i in n1:
    if i == 1:
        n2 = array([2, 3, 4], int)
        Lyman = (R * ((1 / n1 ** 2) - (1 / n2 ** 2)))**(-1)
        print(' the Lyman series with n2 = 1, 2, 3')
        print(Lyman)
    if i == 2:
        n2 = array([3, 4, 5], int)
        Balmer = (R * ((1 / n1 ** 2) - (1 / n2 ** 2))) ** (-1)
        print(' the Balmer series with n2 = 2, 3, 4')
        print(Balmer)
    if i == 3:
        n2 = array([4, 5, 6], int)
        Paschen = (R * ((1 / n1 ** 2) - (1 / n2 ** 2))) ** (-1)
        print(' the Paschen series with n2 = 3, 4, 5')
        print(Paschen)
