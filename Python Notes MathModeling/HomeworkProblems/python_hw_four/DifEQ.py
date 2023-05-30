# 2nd order dif eq
# y'' = f(x, y, y'), y(x_0) = y_0, y'(x_0) = y'_0
#
# y'_1 = y'_0 + f(x0, y0, y'0) delx    eq 20

# ex y" + 2y' + y = 0,    y(0) = 0, y'(0) = 1


# x^2 + 2x + 1 = 0: quadratic eq --> x = -1 & -1
# y = c1e^-x + xc2e^-x
# y(0) = 0 = c1 + c2 (0) --> c1 = 0
# y' = -c1e^-x + -xc2e^-x + c2e^-x
# y'(0) = 1 = -c1 + 0 + c2 = c2 = 1
# sol: y = xe^-x

## program it ##
# on canvas
# note
# optional: ytemp = y
# y=y+yp*dx
# yp=yp+ypp(x,y,yp)*dx  # replace y with ytemp.

# coupled dif equ 1st OD
# ux = f(x, u, v)
# vx = g(x, u, v)
# can be solve via RK4 method
# dy/dx = f(x,y)
# k1 = f(xn, yn)delx
# k2 = f(xn+.5delx, yn+.5k1)delx
# k3 = f(xn+.5delx, yn+.5k2)delx
# k4 = f(xn+delx, yn+k3)delx
# --> yn+1 = yn + 1/6(k1 + 2k2+ 2k3 + k4)

# in 2nd order
# k1 = f(xn, un, vn)delx
# l1 = g(xn, un, vn)delx
# .
# .
# k4 = f(xn+delx, un+k3, vn+l3)delx
# l4 = g(xn+delx, un+k3, vn+l3)delx

# dy/dx = z    play role of u
# dz/dx = f(x, y, z)   ply role of v

# z = z(x) and y = y(x). we dont care about z = z(x)
