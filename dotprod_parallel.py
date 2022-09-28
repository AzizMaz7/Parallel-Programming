from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    a = np.random.randint(10, size=11)
    b = np.random.randint(5, size=11)
    print("proc %d: dot product to compare: %g" %(rank, np.dot(a,b)))
    local_a = np.array_split(a, size)
    local_b = np.array_split(b, size)
    local_dot = 0
    dotvec = 0
    paradot = 0
    dotval = 0
    z = np.dot([],[])
    print("z should be zero: %g" %(z))
else:
    local_a = 0
    local_b = 0
    local_dot = 0
    dotvec = 0
    paradot = 0
    dotval = 0


local_a = comm.scatter(local_a, root=0)
local_b = comm.scatter(local_b, root=0)

print("local_a on proc %d: " %(rank))
print(local_a)
    
print("local_b on proc %d: " %(rank))
print(local_b)

local_dot = np.dot(local_a, local_b)
dotvec = comm.gather(local_dot, root=0)

dotval = np.sum(dotvec)
if rank==0:
    print("after doc prod: proc %d: parallel dotprod = %g " %(rank, dotval))
