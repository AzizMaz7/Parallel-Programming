# code experimented with sleep, wait, isend and irecv
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data1 = {'a': 7, 'b': 3.14}
    data2 = {'c': 8, 'd': 8.14}
    req2 = comm.isend(data2, dest=1, tag=11)
    req2.wait()
    req1 = comm.isend(data1, dest=1, tag=12)
    req1.wait()
    print("processor 0 is done, I am processor %d" %(rank))
elif rank == 1:
    #time.sleep(5)
    reqa = comm.irecv(source=0, tag=11)
    dataa = reqa.wait()
    reqb = comm.irecv(source=0, tag=12)
    datab = reqb.wait()
    print("processor 1 is done, I am processor %d" %(rank))
    print(dataa)
    print(datab)
print("this is out of loop, processor %d" %(rank))
