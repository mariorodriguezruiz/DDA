'''
Created on 9 may. 2017

@author: Mario Rodriguez
'''
import sys
import math
from decimal import *

infinity = 1000

def bbp(i):
    eightI = 8*i
    sixteen = (Decimal(1)/(16**i))
    one = (Decimal(4)/(eightI+1))
    four = (Decimal(2)/(eightI+4))
    five = (Decimal(1)/(eightI+5))
    six = (Decimal(1)/(eightI+6))
    return sixteen*(one-four-five-six)    

def calc_pi(end):
    pi = Decimal(0)
    for i in range(end):
        pi += bbp(i)
    return pi

def main(argv):
    getcontext().prec = (int(infinity))
    pi = bbp(int(infinity))
    print(pi)
#     outfile = open('texto1.txt', 'w') 
#     outfile.write(str(pi)
    
if __name__ == "__main__":
    main(sys.argv[1:])
