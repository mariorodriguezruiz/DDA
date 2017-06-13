# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 12:25:09 2014

@author: Mario Rodríguez Ruiz
"""

import math
import operator
import time
import numpy as np

# only for comprobation
from scipy import spatial

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
    
def getNeighbors(trainingSet, testSet, k):
    distances = []
    for x in range(len(trainingSet)):
        dist = CosineSimilarity(testSet, trainingSet[x])
        distances.append((trainingSet[x], dist, x))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x])
    return neighbors[0]
                
def main():
    # Specification of dimensions    
    ROWS = 9
    COLS = 9
    k = 3
    
    # Creation of matrix Training Set and array Test Set with random integer values
    trainingSet = np.random.randint(100, size=(ROWS, COLS))
    testSet = np.random.randint(100, size=(COLS))
    
    start = time.time()
    neighbor = getNeighbors(trainingSet, testSet, k)    
    end = time.time()
    
    if ROWS <= 10 and ROWS <= 10:
        print('Training Set:\n', trainingSet)
        print('\nTest Set: \n', testSet)
        print('\n__Results__\n1. The maximum cosine similarity\n', (neighbor[1]),
          '\n2. Which training observation that we get the maximum cosine similarity\n', neighbor[0],
          '\nTime of calculation for method that does not implement threads/processes\n', str(end-start))
    else:
        print('\n__Results__\n1. The maximum cosine similarity\n', (neighbor[1]),
          '\n2. (Index of)Which training observation that we get the maximum cosine similarity\n', neighbor[2],
          '\nTime of calculation for method that does not implement threads/processes\n', str(end-start))
        
        
    # only for comprobation    
#     result = 1 - spatial.distance.cosine(trainingSet[neighbor[2]], testSet)
#     print(result)

main()