import numpy as np
import sys
from mpi4py import MPI

PROCESS_INIT = 1
TAM_ARRAY = int(sys.argv[1])

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# ----------- The naive way --------------
comm.Barrier()
start = MPI.Wtime()
if rank == 0:    
    data = np.arange(TAM_ARRAY, dtype='i')
    for i in range(PROCESS_INIT, size):    
        comm.Send([data, MPI.INT], dest=i, tag=11)
        #print ("Array sent from {} to {}".format(rank, i))
else:
    dataRecv = np.empty(TAM_ARRAY, dtype='i')
    comm.Recv([dataRecv, MPI.INT], source=0, tag=11)
    #print ("Array received in {} from {}".format(rank, 0))
    #print(dataRecv)

comm.Barrier()
end = MPI.Wtime()

tim = end-start
totalTime = comm.allreduce(tim, op = MPI.SUM)
MPI.Finalize()

if rank == 0:
    print("Sum processes time naive:\t{}\t{}\t{}".format(size, TAM_ARRAY, (totalTime/size)))