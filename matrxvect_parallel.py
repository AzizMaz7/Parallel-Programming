from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    A = np.random.randint(3, size=(10,12))
    x = np.random.randint(3, size=12)
    print("actual Ax")
    print(np.dot(A,x))
    m = len(A) # num rows of A
    local_x = np.array_split(x, size)
else:
    local_x = 0
    m = 0

local_x = comm.scatter(local_x, root=0)

m = comm.bcast(m, root=0)
b = np.zeros(m)

for i in range(m):
    if rank ==0:
        a = A[i]
        local_a = np.array_split(a, size)
    else:
        local_a = 0

    local_a = comm.scatter(local_a, root=0)
    local_dot = np.dot(local_a, local_x)
    dotvec = comm.gather(local_dot, root=0)
    if rank == 0:
        b[i] = np.sum(dotvec)
    
b = comm.bcast(b, root=0)
print(b)
