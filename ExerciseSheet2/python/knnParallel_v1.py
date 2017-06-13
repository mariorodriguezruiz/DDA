# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 12:25:09 2014

@author: Mario Rodríguez Ruiz
"""

import math
import operator
import time
from multiprocessing import Pool, freeze_support
import numpy as np

# only for comprobation
from scipy import spatial
NUM_TH = 8

# Cosine similarity calculation of A to B: (A * B)/(|A|*|B|)"
def CosineSimilarity(A, B):    
    sumX, sumXY, sumY = 0, 0, 0
    # For all size of A or B
    for i in range(len(A)):
        x = A[i]
        y = B[i]
        sumX += x*x
        sumY += y*y
        sumXY += x*y
    # return (A * B)/(|A|*|B|)
    return sumXY/math.sqrt(sumX*sumY) 
    
def getNeighbors(trainingSet, testSet, k, proc):
    distances = []
    for x in range(len(trainingSet)):
        with Pool(proc) as pool:
            L = pool.starmap(CosineSimilarity, [(testSet, trainingSet[x])])
        dist = 1 - L[-1]
        distances.append((trainingSet[x], dist, x))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x])
    return neighbors[0]
                
def main():
    # Specification of dimensions    
    ROWS = 10
    COLS = 10
    k = 3
    
    # Creation of matrix Training Set and array Test Set with random integer values
    trainingSet = np.random.randint(10, size=(ROWS, COLS))
    testSet = np.random.randint(10, size=(COLS))
          
    # only for comprobation    
#     result = 1 - spatial.distance.cosine(trainingSet[neighbor[2]], testSet)
#     print(result)
    res = []
    times = []
    nt = 1
    for i in range(nt, NUM_TH+1):
        start = time.time()    
        vec = getNeighbors(trainingSet, testSet, k, i)
        end = time.time()
        res.append(vec)
        times.append(end-start)
    
    # Prints results
    print('\nCosine similarity MAX\tTraining observation index\tTime\tProcesses')
    for i in range(len(res)):
        print(round(res[i][1], 4), '\t', res[i][2], '\t', round(times[i], 4), '\t', i+1)
    
#     vec = L.get()
    
#     if ROWS <= 10 and COLS <= 10:
# #         print('Training Set:\n', trainingSet)
# #         print('Test Set: ', testSet)
#         print('\n__Parallel program results__\n1. The maximum cosine similarity\n', vec[1],
#           '\n2. Which training observation that we get the maximum cosine similarity\n', vec[0],
#           '\nTime of calculation for method that does not implement threads/processes\n', str(end-start))
#     else:
#         print('\n__Parallel program results__\n1. The maximum cosine similarity\n', vec[1],
#           '\n2. (Index of)Which training observation that we get the maximum cosine similarity\n', vec[2],
#           '\nTime of calculation for method that does not implement threads/processes\n', str(end-start))

if __name__=="__main__":
    freeze_support()
    main()