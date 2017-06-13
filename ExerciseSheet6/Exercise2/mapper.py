'''
Created on 21 may. 2017

@author: Mario
'''
import sys
import re
import os

# input comes from STDIN
for line in sys.stdin:
    # remove anything other than an alphabet letter
    line = re.sub('[^A-Za-z]+', ' ', line)
    # converts the text to lowercase 
    line = line.lower()
    # split the line into words
    words = line.split()
    # storage line for english words
    en_words = line
    
    # Find the name of the input file
    try:
        input_file = os.environ['mapreduce_map_input_file']
    except KeyError:
        input_file = os.environ['map_input_file']
    
    # if line size is high than 550 it is because
    # the text file is the common english words 
    if(len(line)>550):
        # write the results to STDOUT
        print ('{}\t{}\t{}'.format(en_words, 0, input_file))
    else:
        # For each word of the line
        for word in words:
            if len(word)>1:
                # write the results to STDOUT    
                print ('{}\t{}\t{}'.format(word, 1, input_file))