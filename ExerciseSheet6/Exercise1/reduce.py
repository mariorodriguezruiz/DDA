'''
Created on 21 may. 2017

@author: Mario
'''
import sys

current_word = None
current_count = 0
word = None
common_english_words = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    # Converts input to numeric value
    count = int(count)
    # If count is zero it means that the input is the Common English
    if count == 0:
        common_english_words = word.split(' ')
    # if count is one means that the entry is now the word bank
    elif count == 1:
        # it works because Hadoop sorts map output
        # by key (word) before it's passed to the reducer
        if current_word == word:
            current_count += count
        # If the word isn't a Common English
        elif word not in common_english_words:
            if current_word:
                # write result to STDOUT
                print ('{}\t{}'.format(current_word, current_count))
            current_count = count
            current_word = word    

# write the last word if needed
if current_word == word:
    print ('{}\t{}'.format(current_word, current_count))