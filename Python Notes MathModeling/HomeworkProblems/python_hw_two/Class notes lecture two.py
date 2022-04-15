from math import *

# this file is used for class notes for homework 6.

# containers are used to store tensors of rank 0, 1, 2, ...
# these involve, lists and arrays
# making a list example can have rational values
r = [2, 3, -5]
print(r)

# display 2nd term or element 1
print(r[1])

# find sum of elements in a list
print(sum(r))

# maximum minimum length
print(max(r)), print(min(r)), print(len(r))

# variable list
x = 1
y = 2
z = 3
l = [x, y, z]  # x is element 0, y is element 1, z is element 2, and so on ...
print(l)

# python takes angles in radians
# sine of a list.
from math import *

r = [1, 2, 4]
new = list(map(sin, r))
print(new)

# appending and removing elements
r = [1]
print(r)
r.append(5)  # adds element
print(r)
r.pop(1)  # removes element n
print(r)

print(10 * '~')
# arrays
# once the array is made, you cannot change the number of elements (append and pop do not work)
# making an array must be floating or integers, you can replace elements with another
# a list is one dimensional, but array can be multidimensional
# arrays behave like vectors and matrices, lists cannot do this

# new package install
# arrays examples
from numpy import *

a = zeros(5, int)  # array of 5 zeros as integer values (int or float)
print(a)
b = zeros([8, 6], float)  # array of 8 x 6 float
print(b)

# array command
c = array([[1, 2, 3], [4, 5, 6], [3.2, 5.6, -3.5]], float)  # converts list to array
print(c)
# float and int are not needed the array will convert based on the first lists entry

d = array([[1.4, 2.6, 3.8], [4, 5, 6]], int)  # no rounding, drops anything after decimal
print(d)

# wait command

# wait = input('press enter to continue')
# example
x = array([[1, 2, 3], [4, 5, 6]], int)
print(x)
wait = input('press enter to continue')
x[1, 2] = -10  # replace the 6 with -10 as 1,2 is the element 6 in the 3x2 array
print(x)

# sleep command (time wait)
import time

x = array([[1, 2, 3], [4, 5, 6]], int)
print(x)
time.sleep(2)  # program sleeps for 2 seconds
x[1, 2] = -10
print(x)

# changing element of array
g = zeros([3, 3], int)
print(g)

g[0, 0] = 1
g[1, 1] = 1
g[2, 2] = 1
print(g)


