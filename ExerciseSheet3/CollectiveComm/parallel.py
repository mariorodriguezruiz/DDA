import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpi4py import MPI
 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

gray_img = cv2.imread ('C:\\Users\\Mario\\Desktop\\je.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('GoldenGate',gray_img)
grey_levels = 256

# Start time
comm.Barrier()
start = MPI.Wtime()

# Maximum number of height pixels per process
# height of image (3000) / number of processes
y_advances = int(gray_img.shape[0]/size)

# Maximum number of width pixels per process
# width of image (4500) / number of processes
x_advances = int(gray_img.shape[1]/size)

# Index that controls the start of pixels height
y_ini = int((rank-1)*y_advances)

# Index that controls the end of pixels height
y_fin = y_advances*rank

# Index that controls the start of pixels width
x_ini = (rank-1)*x_advances

# Index that controls the end of pixels width
x_fin = x_advances*rank       

# For the entire range of height and width corresponding to a process
# a portion of pixels is extracted and 
# then the histogram is calculated for this portion.
for r in range(y_ini, y_fin):
    for c in range(x_ini, x_fin):
        portion = gray_img[r:r+size,c:c+size]
        hist = np.histogram(portion,bins=grey_levels)

hist = comm.gather(hist, root=0)
    
comm.Barrier()
end = MPI.Wtime()
tim = end-start
totalTime = comm.allreduce(tim, op = MPI.SUM)

if rank== 0:
    MPI.Finalize()
    print("Sum processes time:\t{}\t{}".format(size, (totalTime/size)))
#     plt.hist(gray_img.ravel(),256,[0,256])
#     plt.title('Histogram for gray scale picture')
#     plt.show()
#        
#     while True:
#         k = cv2.waitKey(0) & 0xFF     
#         if k == 27: break             # ESC key to exit 
#     cv2.destroyAllWindows()
    
