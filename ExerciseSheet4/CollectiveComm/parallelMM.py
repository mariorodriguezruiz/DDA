'''
Created on 9 may. 2017

@author: Mario Rodriguez
'''
from mpi4py import MPI
import numpy

# MPI common values between processes
comm = MPI.COMM_WORLD
size = comm.Get_size()
# MPI single values of a process
rank = comm.Get_rank()    

# To make a correct division of labor, the dimension of 
# the matrix must be a multiple of the number of processes.
SIZE_ROWS = int(1920*2)
ROWS = int(numpy.ceil(SIZE_ROWS/size)*size)
COLS = int(1920)

# Rows to calculate per each process
n_calc = int(ROWS/size)
# matrix initialized to scatter communication (matrix_A chunks)
chunk_A = numpy.zeros((n_calc,COLS),dtype='i')
# matrix initialized to save the result (gatter)
matrix_C = numpy.zeros((ROWS,ROWS),dtype='i')

if rank==0:
    # Creating matrices with integer random values
    matrix_A = numpy.random.randint(4, size=(ROWS,COLS))
#     print('\nmatrix_A:\n',matrix_A)
    matrix_B = numpy.random.randint(4, size=(COLS,ROWS))
#     print('\nmatrix_B:\n',matrix_B)    
else:
    # Creating matrices buffers
    matrix_A = numpy.zeros((ROWS,COLS),dtype='i')
    matrix_B = numpy.zeros((COLS,ROWS),dtype='i')

# Start time for a process
comm.Barrier()
start = MPI.Wtime()

# Broadcast of matrix_B (the same data to all processes)
comm.Bcast([matrix_B,MPI.INT])
# Scatter of matrix_A (matrix_A chunks of data to each process)
comm.Scatter([matrix_A,MPI.INT],[chunk_A,MPI.INT])
# Chunk multiplication 
chunk_C = numpy.dot(chunk_A,matrix_B)  
# Saving the chunk multiplication in the result matrix (matrix_C)
comm.Gather([chunk_C,MPI.INT],[matrix_C,MPI.INT])

# End time for a process
comm.Barrier()
tim = MPI.Wtime()-start

# Sum of time of all processes 
totalTime = comm.allreduce(tim, op = MPI.SUM)

if rank==0:    
    MPI.Finalize()
#     print('\nmatrix_C:\n',matrix_C)
    print("Dimensions:\n\tmatrix_A = {}*{}\n\tmatrix_B = {}*{}\n\tmatrix_A*B = {}*{}".format(ROWS, COLS, COLS, ROWS, ROWS, ROWS))
    print("\n__Sum processes time__")
    print("\tProcesses\tTime(seconds)")
    print("\t{}\t{}".format(size, (totalTime/size)))
