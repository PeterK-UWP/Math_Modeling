# problem 6
from numpy import *
import numpy as np
from math import *

# geometric_mean = exp((1/n) * sum(ln(x_k))
a = loadtxt('data_rms.txt', int)   # load 1-10 in rms file

for i in a:
    sum_natural_log = sum(np.log(a))  # sum of natural logs from n = 1 to 10
# print(sum_natural_log)
exponent = 1/10 * sum_natural_log  # n = 10
# print(exponent)
geometric_mean = np.exp(exponent)
print(f' the geometric mean of a is: {geometric_mean:0.3f}')
