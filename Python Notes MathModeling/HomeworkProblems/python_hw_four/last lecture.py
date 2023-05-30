# x = 0
# x_n = (a * x_n-1 + b)mod m, n = 1, 2, 3, ...

import matplotlib.pyplot as mp

N = 100
a = 1664525
b = 1013904223
m = 4294967296
x = 1  # seed
results = []
for i in range(N):
    x = (a * x + b) % m
    results.append(x)
mp.plot(results, 'o')
mp.show()

# package: random
# random()

# simulation of nuclear decay
# dN = lambda * N dt
# N = N0 * exp(-lambda * t)
# t1/2 = ln(2)/lambda
# monte carlo
from numpy import
from random import
import matplotlib.pyplot as mp
N0 = 500
N0temp = N0
tmax = 500
p = 0.01

tdata = []
Ndata = []
tdata.append(0)
Ndata.append(N0)

N = N0
