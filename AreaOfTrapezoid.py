# code for calculating area of trapezoid using 1 processor
from mpi4py import MPI
import sys
import numpy as np

# serial

# Integral 0 to pi of sin(x) using trapezoidal rule and 11 evenly spaced
# points.

a = 0                          # left endpoint
b = np.pi                      # right endpoint
n = 10                         # number of intervals
h = (b - a) / (n)          # width of base
x = np.linspace(a, b, n+1)       # n equally spaced grid points between a and b
f = np.sin(x)                  # sin(x), height 

I_trap = (h/2)*(f[0] + 2 * sum(f[1:n]) + f[n])

# correct answer is 2
err_trap = 2 - I_trap

# print answer
print(I_trap)

# print error
print(err_trap)
