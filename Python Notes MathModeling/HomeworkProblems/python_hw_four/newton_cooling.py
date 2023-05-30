# problem two
# a) Analytically solve the differential equation of Newton’s law of cooling to obtain Eq. (11).
# (b) How long does it take the object to reach the surrounding temperature? (c) In terms of
# k, how long does it take for temperature of the object to drop to half way between its initial
# value and the surrounding temperature (we can call this half-life of cooling)?

# dT/dt = -k(T-T_s)    T(0) = T_0
# ln(T-T_s) = -kT + C
# T-T_s = Ae^(-kt) --> T = T_s + Ae^(-kt)
# A = T_0 - T_s
# T = T_s + (T_0 - T_s)e^(-kt)  T(t)

# T = T_s ?
# T_s = T_s + (T_0 - T_s)e^(-kt)
# 0 = (T_0 - T_s)e^(-kt) , (T_o - T_s) != 0
# 0 = e^(-kt)
# t = inf.

# (T_0 + T_s)/ 2 = T_s + (T_0 - T_s)e^(-kt)
# T_0/2 + T_s/2 = T_s + (T_0 - T_s)e^(-kt)
# # T_0/2 - T_s/2 =  (T_0 - T_s)e^(-kt)
# 1/2 = e^(-kt)
# t = ln(2)/k
