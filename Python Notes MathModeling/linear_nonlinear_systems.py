# linear equation: y = mx + b
# linear differential equation: y = mx
# linear dif eq can have nonlinear solutions such as e^x

# Newtons Law of Cooling
"""
dT/dt = -k(T - T_s)
T - temp of object
T_s - temp of surrounding
k - cooling constant [Hz]
Let T(0) = T_0
solve with Separation of Variables:
    T = Ae^{-kt} + T_s
    T_0 = A + T_s -> A = T_0 - T_s
    T = (T_0 - T_s)e^{-kt} + T_s
    note as t -> infinity: T = T_s
    non-dimensionalize:
    T/T_s = (T_0/T_s - 1)e^{-kt} + 1
"""
