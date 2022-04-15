# problem 8
from math import *
print('enter value to get degeneracy')
total_n_squared = eval(input('input: '))  # nx^2 + ny^2 + nz^2
print('n=', total_n_squared)
square_root_n_squared = int(sqrt(total_n_squared))
degeneracy = 0
for nx in range(1, square_root_n_squared + 1):
    for ny in range(1, square_root_n_squared + 1):
        for nz in range(1, square_root_n_squared + 1):
            if nx**2 + ny**2 + nz**2 == total_n_squared:
                print(nx, ny, nz)
                degeneracy = degeneracy + 1
if degeneracy > 2:
    print('degeneracy=', degeneracy)





