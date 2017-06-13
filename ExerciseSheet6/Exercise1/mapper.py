'''
Created on 21 may. 2017

@author: Mario
'''
import sys
import re

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
    
    # if line size is high than 550 it is because
    # the text file is the common english words 
    if(len(line)>550):
        print ('{}\t{}'.format(en_words, 0))
    # it is the text file to evaluate
    else:
        # each word found in the data file
        for word in words:
            if len(word)>1:
                # write the results to STDOUT    
                print ('{}\t{}'.format(word, 1))
