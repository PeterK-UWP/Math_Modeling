# problem 3
# write a program that utilizes stirlings approximation
# ln(N!) = Nln(N) - N, N >> 1
from math import *
n = 1000  # input very large n
summ = 0
for i in range(1, n+1):
    summ = summ + log(i)  # sum k=1 n (lnk)
x = summ
y = n * (log(n) - 1)
print(n, ' ', x/y)
