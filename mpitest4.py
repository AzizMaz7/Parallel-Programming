# code experimented with broadcast, scatter and gather
from mpi4py import MPI
import time
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    data2 = np.linspace(1,4,4)
    print(data2)
    
else:
    data = None
    data2 = None
    
data3 = rank
print("proc %d, data3 " %(rank))
print(data3)

data4 = comm.allgather(data3)
print("after gather")
print("proc %d, data4 " %(rank))
print(data4)
