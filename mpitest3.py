# code experimented with send/recv and isend/irecv
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print("proc 0 is starting")
    data1 = {'a': 7, 'b': 3.14}
    data2 = {'c': 8, 'd': 8.14}
    #time.sleep(5)
    comm.ssend(data1, dest=1, tag=11)
    #req2.wait()
    print("proc 0 message 11 sent")
    time.sleep(3)
    comm.ssend(data2, dest=1, tag=12)
    #req1 = comm.isend(data1, dest=1, tag=12)
    #req1.wait()
    print("proc 0 message 12 sent")
    print("proc 0 is done")
elif rank == 1:
    print("proc 1 is starting")
    datab = comm.recv(source=0, tag=11)
    print("proc 1 message 11 received")
    print(datab)
    time.sleep(6)
    #dataa = reqa.wait()
    dataa = comm.recv(source=0, tag=12)
    #reqb = comm.irecv(source=0, tag=12)
    #datab = reqb.wait()
    print("proc 1 message 12 received")
    print(dataa)
    print("proc 1 is done; I am proc %d" %(rank))
print("this is out of the loop, proc %d" %(rank))
