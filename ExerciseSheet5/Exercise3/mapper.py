'''
Created on 16 may. 2017

@author: Mario Rodriguez
'''
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split('::')
    
    movies_id = "-1"
    movies_ratings = "-1"
    title = "-1"
    movies_id_tit = "-1"
    users_id = "-1"
    gnres = "-1"
    
    # ratings data
    # UserID::MovieID::Rating::Timestamp
    #  ^^^      ^^^      ^^^
    # line[0] line[1]  line[2]
    if len(line) == 4: 
        users_id = line[0]
        movies_id = line[1]
        movies_ratings = line[2]
    # movies data
    # MovieID::Title::Genres
    #   ^^^      ^^^   ^^^
    # line[0]  line[1] line[2]
    elif len(line) > 1: 
        movies_id_tit = line[0]
        title = line[1]   
        gnres = line[2]

    print ("{}\t{}\t{}\t{}\t{}\t{}".format(movies_id, movies_ratings, movies_id_tit, title, users_id, gnres))
