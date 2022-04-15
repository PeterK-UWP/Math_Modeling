from math import *
# question 5
# calculate probabilities and find their sum given the following equations.
print('f is given by potential (V) over kinetic energy (K) with K > V')
print('f = V/K, f < 0')
f = eval(input('enter f:'))
probability_of_transmission = 4*sqrt(1-f) / (1 + sqrt(1-f))**2
probability_of_reflection = (1 - sqrt(1-f))**2 / (1 + sqrt(1-f))**2
print(f'probability by transmission is      {probability_of_transmission:0.4f}')
print(f'probability by reflection is        {probability_of_reflection:0.4}')
print(f'the sum of the two probabilities is {(probability_of_transmission + probability_of_reflection):0.4f}')
