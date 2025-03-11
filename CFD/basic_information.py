import numpy as np

"""
created on Thurs Nov. 7 4:00:00 2024

@ author: Peter Kveton
Tanmay Agrawal YouTube Course - Simulating Fluid Flows Using Python 
"""

# Scalars
a = 1  # without numpy
anum = np.int32(1)  # 32 bit integer
print(f'a = {a} is a {type(a)}, and anum = {anum} is a {type(anum)}')

# Float
b = 0.1 # w/o numpy
bnum = np.float64(0.1)  # 64 bit float
print(f'b = {b} is a {type(b)}, and bnum = {bnum} is a {type(bnum)}')

# Array - integer
c = [1, 2, 3]  # w/o numpy - list
c_array = np.array([1, 2, 3])  # numpy array, not a list, better computationally
print(f'c = {c} is a {type(c)}, and c array = {c_array} is a {type(c_array)}')

# Array - float
d = [1.1, 2, 3]  # w/o numpy
d_array = np.array([1.1, 2, 3])
print(f'd = {d} is a {type(d)}, and d array = {d_array} is a {type(d_array)}')