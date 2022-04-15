from math import *

# question 6
# given N, sum up even / odd numbers less than or equal too.
print('enter an even number')
n = eval(input('enter n:'))  # 16 is 72
sum_even = 0
for i in range(2, n + 2, 2):  # from 2 to n+2 in increments of 2
    sum_even = sum_even + i
print(f'the sum of even values up to {n} is: {sum_even}')

print('enter an odd number')
m = eval(input('enter m:'))  # 9 is 25
sum_odd = 0
for j in range(1, m + 2, 2):
    sum_odd = sum_odd + j
print(f'the sum of odd values up to {m} is: {sum_odd}')
