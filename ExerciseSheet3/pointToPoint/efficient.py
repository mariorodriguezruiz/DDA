import numpy as np
import sys
from mpi4py import MPI

PROCESS_INIT = 1
TAM_ARRAY = int(sys.argv[1])

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ----------- The efficient way --------------
comm.Barrier()
start = MPI.Wtime()
if rank == 0:
    data = np.arange(TAM_ARRAY, dtype='i')              
    for i in range(PROCESS_INIT, 3):
        comm.Send([data, MPI.INT], dest=i, tag=11)
        #print ("Array sent from {} to {}".format(rank, i))
else:
    dataRecv = np.empty(TAM_ARRAY, dtype='i')
    recvProc = int((rank-1)/2)
    comm.Recv([dataRecv, MPI.INT], source=recvProc, tag=11)
    #print ("Array received in {} from {}".format(rank, recvProc))
    #print(dataRecv)
    
    destA = 2*rank + 1    
    if destA < size:
        comm.Send([dataRecv, MPI.INT], dest=destA, tag=11)
        #print ("Array sent from {} to {}".format(rank, destA))
        
    destB = 2*rank + 2
    if destB < size:
        comm.Send([dataRecv, MPI.INT], dest=destB, tag=11)
#         print ("Array sent from {} to {}".format(rank, destB))
    
comm.Barrier()
end = MPI.Wtime()

tim = end-start
totalTime = comm.allreduce(tim, op = MPI.SUM)
MPI.Finalize()
     
if rank == 0:
    print("Sum processes time efficient:\t{}\t{}\t{}".format(size, TAM_ARRAY, (totalTime/size)))