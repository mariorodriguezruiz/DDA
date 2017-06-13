'''
Created on 17 abr. 2017

@author: Mario Rodríguez
'''

import time, math
import random
import numpy as np

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
def MiniumNumber(v):
    mini = v[0]
    i = 0    
    for i in range(len(v1)):
        if v[i] < mini:
            mini = v[i]
    return mini

# Find an average of numbers in a vector
def Average(v):
    tam = len(v)
    av = 0
    i = 0    
    for i in range(tam):
        av = av + v[i]
    return av/tam

if __name__ == '__main__':
#     tam = math.pow(10, 7)
#     tam = math.pow(10, 8)
    tam = math.pow(10, 8.5)
    v1 = CreateVector(tam)
    v2 = CreateVector(tam)   
    
    # ------------------- EXPERIMENT a) ------------------------------
    
    outfile = open('..\prints\printsSeq.txt', 'a')
    outfile.write('\n__Add two vectors and store results in a third vector__\n')
    
    start = time.time()
    v3 = AddVectors(v1, v2)
    end = time.time()      
    
    outfile = open('..\prints\printsSeq.txt', 'a')  
    outfile.write('Size \tRun1 (s) \n')
    outfile.write(str(tam))  
                 
    t = end-start
    
    outfile = open('..\prints\printsSeq.txt', 'a')      
    outfile.write('\t' + str(t)) 
    
# ------------------- EXPERIMENT b) ------------------------------    
     
     
    outfile = open('..\prints\printsSeq.txt', 'a')
    outfile.write('\n__Find a minimum number in a vector__\n')
    
    start = time.time()
    res = MiniumNumber(v2)
    end = time.time()      
    t = end-start
    
    outfile = open('..\prints\printsSeq.txt', 'a')  
    outfile.write('Size \tResult \tRun1 (s) \n')
    outfile.write(str(tam) + '\t' + str(res) + '\t' + str(t)) 
     
# ------------------- EXPERIMENT c) ------------------------------    
     
    outfile = open('..\prints\printsSeq.txt', 'a')
    outfile.write('\n__Find an average of numbers in a vector__\n')
    
    start = time.time()
    res = Average(v1)
    end = time.time()   
    t = end-start   
     
    outfile = open('..\prints\printsSeq.txt', 'a')  
    outfile.write('Size \tResult \tRun1 (s) \n')
    outfile.write(str(tam) + '\t' + str(res) + '\t' + str(t))      
     
    # -------------------------------------------
#     print(v1)
#     print(v2)
#     print(v3)
#     print(miniumnumber(v2))
#     print(average(v1))
    
    outfile.close()
