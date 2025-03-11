import numpy as np

"""
created on Thurs Nov. 7 4:00:00 2024

@ author: Peter Kveton
Tanmay Agrawal YouTube Course - Simulating Fluid Flows Using Python 

f(x) = -4x^3 + 7x^2 - 3x + 9
f'(x) = -12x^2 + 14x - 3
f'(0) = 3
"""

# Finite Difference Methods
# For a polynomial based function in python:
# Write coefficients of f(x) in a 1D array
poly_coeffieicnt = np.array([-4, 7, -3, 9])

# Write f'(x) as a np.polyder(array)
derivative = np.polyder(poly_coeffieicnt)

# Write f'(0) as a np.polyval(polynomial, x_0)
derivative_zero = np.polyval(derivative, 0)

# Initial Inputs
x0 = 0.0
h = 0.25
inverse_h = 1 / h

# Forward Difference
forward_difference = (np.polyval(poly_coeffieicnt, x0 + h) - np.polyval(poly_coeffieicnt, x0)) * inverse_h

# Backward Difference
backward_difference = (np.polyval(poly_coeffieicnt, x0) - np.polyval(poly_coeffieicnt, x0 - h)) * inverse_h

# Central Difference
central_difference = (np.polyval(poly_coeffieicnt, x0 + h) - np.polyval(poly_coeffieicnt, x0 - h)) * 0.5 * inverse_h

# Results
print(f'forward {forward_difference}')
print(f'forward {backward_difference}')
print(f'forward {central_difference}')
print(f'actual {derivative_zero}')