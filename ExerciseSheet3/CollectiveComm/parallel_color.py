import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpi4py import MPI
 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

img = cv2.imread('C:\\Users\\Mario\\Desktop\\je.jpg', -1)
# cv2.imshow('GoldenGate',gray_img)
grey_levels = 256
color = ('b','g','r')
# Define the window size
comm.Barrier()
start = MPI.Wtime()
y_advances = int(img.shape[0]/size)
x_advances = int(img.shape[1]/size)
y_ini = int((rank-1)*y_advances)
y_fin = y_advances*rank
x_ini = (rank-1)*x_advances
x_fin = x_advances*rank       
for r in range(y_ini, y_fin):
    for c in range(x_ini, x_fin):
        for channel,col in enumerate(color):
            window = img[r:r+size,c:c+size]
            hist = cv2.calcHist([window],[channel],None,[256],[0,256])
            plt.plot(hist,color = col)
            

hist = comm.gather(hist, root=0)
    
comm.Barrier()
end = MPI.Wtime()
tim = end-start
totalTime = comm.allreduce(tim, op = MPI.SUM)

if rank== 0:
    MPI.Finalize()
#     print("Sum processes time:\t{}\t{}".format(size, (totalTime/size)))
    plt.xlim([0,256])
    plt.title('Histogram for color scale picture')
    plt.show()
    
    while True:
        k = cv2.waitKey(0) & 0xFF     
        if k == 27: break             # ESC key to exit 
    cv2.destroyAllWindows()
    
