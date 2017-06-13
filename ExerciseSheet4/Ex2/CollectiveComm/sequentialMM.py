'''
Created on 9 may. 2017

@author: Mario Rodriguez
'''
import numpy as np

ROWS_1 = 2
COLS_1 = 3
ROWS_2 = COLS_1
COLS_2 = 4
 
def mm(matrix_A, matrix_B):
    matrix_C = np.zeros((ROWS_1,COLS_2))
    for i in range(ROWS_1):
        for j in range(COLS_2):
            for k in range(COLS_1):
                matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
    return matrix_C

def main():
    matrix_A = np.random.randint(4, size=(ROWS_1,COLS_1))
    matrix_B = np.random.randint(4, size=(ROWS_2,COLS_2))
    matrix_C = mm(matrix_A, matrix_B)    
    
    print (matrix_A)
    print (matrix_B)    
    print (matrix_C)

if __name__ == '__main__':
    main()