'''
Created on 9 may. 2017

@author: Mario Rodriguez
'''
import numpy as np
from decimal import *
from mpi4py import MPI
 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Value of infinity
infinity = 100000

# Calculate calculation limits for each process
def limits():
    # Number of calculations for each process
    n_calc = int(infinity/size)
    # Remainder of the division of the calculations of each process
    rest = int(infinity % size)
    
    # If there is a remainder, it is divided into 
    # one unit per process until do all allotted.
    if rest != 0:
        if rank < rest :
            # Whenever an additional unit is assigned to a process, both the 
            # start position and the end position of the other processes will be affected.
            n_calc = n_calc + 1
            if rank == 0:
                ini = 0
            else:
                ini = rank*n_calc
        else:
            ini = rank*n_calc+rest
    else:
        ini = rank*n_calc    
    end = ini + n_calc
    return ini,end

# Bailey-Borwein-Plouffe formula
def bbp(i):
    eightI = 8*i
    sixteen = (Decimal(1)/(16**i))
    one = (Decimal(4)/(eightI+1))
    four = (Decimal(2)/(eightI+4))
    five = (Decimal(1)/(eightI+5))
    six = (Decimal(1)/(eightI+6))
    return sixteen*(one-four-five-six)    

def calc_pi(i , end):
    pi = Decimal(0)
    for i in range(i, end):
        pi += bbp(i)
    return pi

# Start time for a process
comm.Barrier()
start = MPI.Wtime()

# Calculation limits for each process
ini, end = limits()
# User alterable precision (infinity)
getcontext().prec = (int(infinity)) 
pi = calc_pi(ini, end)
total_pi = comm.allreduce(pi, op = MPI.SUM)

# End time for a process
comm.Barrier()
end = MPI.Wtime()
tim = end-start

# Sum of time of all processes 
totalTime = comm.allreduce(tim, op = MPI.SUM)

if rank== 0:
    MPI.Finalize()
#     outfile = open('texto.txt', 'w') 
#     outfile.write(str(total_pi))
#     print("Pi:\t", total_pi)
    print("Sum processes time:\t{}\t{}".format(size, (totalTime/size)))
