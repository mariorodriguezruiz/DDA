'''
Created on 16 may. 2017

@author: Mario Rodriguez
'''
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    origin = line[3]
    dep_delay = line[6]
    arr_delay = line[8]

    print ("{}\t{}\t{}".format(origin, dep_delay, arr_delay))
