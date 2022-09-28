# code for calculating area of trapezoid using prallel programming
from mpi4py import MPI
import sys
import numpy as np

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
comm=MPI.COMM_WORLD

# parallel version of trapezoidal rule

# same on all processes
a = 0                          # left endpoint
b = np.pi                      # right endpoint
n = 10                         # number of trapezoids
h = (b - a) / (n)          # width of base

if rank == 0:
    
    local_n_value = int(n/size)
    local_n = [local_n_value]*size
    local_a = [0]*size
    leftover = n%size #mod

    counter = 0
    counter_ntotal = 0
    for i in range(leftover):
        local_n[counter%size] += 1
        local_a
        counter += 1
    for i in range(size):
        local_a[i] = a + counter_ntotal*h
        counter_ntotal += local_n[i]

else:
    local_n = 0
    local_a = 0

print(local_n)
    
  
# needed for parallel on each process


local_n = comm.scatter(local_n, root=0)
local_a = comm.scatter(local_a, root=0)

local_b = local_a + local_n*h
local_b = min(local_a + local_n*h, b)

print("proc %d, local_a = %f, local_b = %f" %(rank, local_a, local_b))


# problemn here with indexing on some processes
local_x = np.linspace(local_a, local_b, int(local_n)+1)

local_f = np.sin(local_x)

local_I = (h/2)*(local_f[0] + 2 * sum(local_f[1:int(local_n)]) + local_f[int(local_n)])

print("proc %d local_I = %f" %(rank, local_I))


# Now send all local integrals to process 0 to total
if rank==0:
    total = local_I
    for mysource in range(1, size):
        integral = MPI.COMM_WORLD.recv(source=mysource, tag=11)
        total = total + integral
else:
   MPI.COMM_WORLD.send(local_I, dest=0, tag=11) 


if rank==0:
    print(total)
    err_trap = 2 - total
    print(err_trap)
