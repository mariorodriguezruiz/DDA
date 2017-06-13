'''
Created on 21 may. 2017

@author: Mario
'''
import sys
import math
from textblob import TextBlob as tb

# To save the CEW list
common_english_words = []
# To save the contents of each of the documents
docs = {}
# To save the input file names and use them as indexes
inputs = []
# number of inputs documents (without accounting for the CEW)
n_doc = 0

# term frequency which is the number of times a word appears in a document blob
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

# number of documents containing word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

# inverse document frequency which measures how common a word is among all documents in bloblist
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

# computes the TF-IDF score
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    wordd, count, input_ = line.split('\t')
    # Converts input to numeric value
    count = int(count)
    
    # If count is zero it means that the input is the Common English
    if count == 0:
        common_english_words = wordd.split(' ')
    # If count is one and the name of the input file isn't yet known
    elif count == 1 and input_ not in inputs and wordd not in common_english_words:
        # Save the new name in the list of names
        inputs.append(input_)
        # Initialize new list with index of the new name
        docs[input_] = wordd + ' '
    # If count is one and the word isn't a CEW
    elif count == 1 and wordd not in common_english_words:
        # Add new word to the end of the list identified through the index
        docs[input_] += wordd + ' '

bloblist = []
# Stores the inputs documents (no CEW) in TextBlob format
for i in inputs:
    i = tb(docs[i])
    bloblist.append(i)

# For each word of each document it calculates the TFIDF score 
for i, blob in enumerate(bloblist):
    print("\nTop words in document \"{}\"".format(inputs[i]))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    # sort from highest to lowest list by tfidf scores 
    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("\t--------------")
    print("\tWord\tTF-IDF")
    print("\t--------------")
    for word, score in scores[:3]:
        print("\t{}\t{}".format(word, round(score, 3))) 