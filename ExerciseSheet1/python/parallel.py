'''
Created on 17 abr. 2017

@author: Mario Rodríguez
'''

import time, math
import numpy as np
import threading

RES_MIN = 0
RES_AV = 0
NUM_TH = 8
nt = 1
lock = threading.Lock()

# Create vector with 'size' random values
def CreateVector(size):
    v1 = np.random.rand(int(size))
    return v1

# Add two vectors and store results in a third vector
def AddVectors(v1, v2):
    v3 = []
    i = 0    
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3

# Find a minimum number in a vector
def MiniumNumber(v, pos_ini, pos_fin):
    global RES_MIN
    for pos_ini in range(pos_ini, pos_fin):
        if v[pos_ini] < RES_MIN:
            lock.acquire()
            RES_MIN = v[pos_ini]
            lock.release()

# Find an average of numbers in a vector
def Average(v, i, f):
    global RES_AV
    av = 0
    
    for i in range(f):
        av += v[i]
        
    lock.acquire()
    RES_AV += av/(f-i)
    lock.release()
    
if __name__ == '__main__':
#     tam = math.pow(10, 7)
#     tam = math.pow(10, 8)
    tam = math.pow(10, 7)
    v1 = CreateVector(tam)
    v2 = CreateVector(tam)   
    
#     # ------------------- EXPERIMENT a) ------------------------------
#     
#     outfile = open('..\prints\printParlF.txt', 'a')
#     outfile.write('\n__Add two vectors and store results in a third vector__\n')
#     
#     start = time.time()
#     v3 = AddVectors(v1, v2)
#     end = time.time()      
#     
#     outfile = open('..\prints\printParlF.txt', 'a')  
#     outfile.write('Size \tRun1 (s) \n')
#     outfile.write(str(tam))  
#                  
#     t = end-start
#     
#     outfile = open('..\prints\printParlF.txt', 'a')      
#     outfile.write('\t' + str(t)) 
#     
# ------------------- EXPERIMENT b) ------------------------------      
      
    outfile = open('..\prints\printParlF.txt', 'a')
    outfile.write('\n__Find a minimum number in a vector__\nSize \tResult \tRun (s) \t Threads\n')
    
    # initial nt = 1
    for nt in range(nt, NUM_TH+1): 
        siz = len(v2)/nt        # work size for each thread
        rem_tam = len(v2)%nt    # remainder of division
        RES_MIN = v2[0]         # initialize minium result
        pos_ini = 0
        pos_fin = 0
                         
        start = time.time()    
        for i in range(nt):
            pos_fin = int(pos_ini+siz)  # final position is the sum of initial position and work size 
            t = threading.Thread(target=MiniumNumber, args=(v2, pos_ini, pos_fin))
            pos_ini = pos_fin # update initial position for next thread
            t.start()
            t.join()
        
        # When remainder is distint of zero
        if rem_tam > 0:
            for i in range(rem_tam):
                pos_fin = pos_ini+1
                t = threading.Thread(target=MiniumNumber, args=(v2, pos_ini, pos_fin))
                pos_ini = pos_fin
                t.start()
                t.join() 
           
        end = time.time()
        tim = end-start
        
        outfile.write(str(tam) + '\t' + str(RES_MIN) + '\t' + str(tim) + '\t' + str(nt) + '\n') 
    outfile.close()
#     #      
# # ------------------- EXPERIMENT c) ------------------------------    
#      
#     outfile = open('..\prints\printParlF.txt', 'a')
#     outfile.write('\n__Find an average of numbers in a vector__\n \nSize \tResult \tRun (s) \t Threads\n')
#     
#     # initial nt = 1
#     for nt in range(nt, NUM_TH+1): 
#         siz = len(v2)/nt    # work size for each thread
#         rem_tam = len(v2)%nt   # remainder of division
#         pos_ini = 0
#         pos_fin = 0
#                         
#         start = time.time()    
#         for i in range(nt):
#             pos_fin = int(pos_ini+siz)  # final position is the sum of initial position and work size 
#             t = threading.Thread(target=Average, args=(v2, pos_ini, pos_fin))
#             pos_ini = pos_fin # update initial position for next thread
#             t.start()
#             t.join()
#         
#         # When remainder is distint of zero
#         if rem_tam > 0:
#             for i in range(rem_tam):
#                 pos_fin = pos_ini+1
#                 t = threading.Thread(target=Average, args=(v2, pos_ini, pos_fin))
#                 pos_ini = pos_fin
#                 t.start()
#                 t.join() 
#           
#         end = time.time()
#         tim = end-start      
#     
#     outfile.write(str(tam) + '\t' + str(RES_AV) + '\t' + str(tim) + '\t' + str(nt) + '\n')       
     
    # -------------------------------------------
    if tam<=10:
        print(v1)
        print(v2)
        print(RES_MIN)
#         print(v3)
#         print(MiniumNumber(v2))
#         print(average(v1))
    
    
