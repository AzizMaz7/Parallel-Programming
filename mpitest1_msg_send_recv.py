from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

if rank==0:
    msg = "Hello, World"
    comm.send(msg, dest=1, tag=11)
    
elif rank==1:
    s= comm.recv(source=0, tag=11)
    print("rank %d: %s" % (rank, s))
