'''
Created on 16 may. 2017

@author: Mario Rodriguez
'''
import sys

movies_id_ratings = {}
movies_id_title = {}
users_ratings = {}
movies_id_gnres = {}

# Create the corresponding lists and then 
# find a movie according to your rating
def createListsMovRatings(movies_id, movies_ratings, id_tit, title):
    # If title isn't trash 
    if title != "-1":
        # If yet exists this movie_id
        if id_tit not in movies_id_title:
            # Add new title to the lists with id_tit like index
            movies_id_title[id_tit] = title
    # If movies_id isn't trash     
    elif movies_id != -1:    
        # If already exists this movie_id
        if movies_id in movies_id_ratings:
            # Add new rating to the list of this movie_id
            movies_id_ratings[movies_id].append(movies_ratings)
        # If this origin does not yet exist    
        else:
            # Create two new rating list with movies_id like index
            movies_id_ratings[movies_id] = []
            # Add the first rating to the lists
            movies_id_ratings[movies_id].append(movies_ratings)

# Movie title which has the maximum average rating
def movieMaxAvgRating():
    result = [0, 0]
    # Calculation of ratings averages for each movie
    # Storing averages in a list along with your ID 
    for movie_id in movies_id_ratings.keys():    
        avg_movie_ratings = sum(movies_id_ratings[movie_id])*1.0 / len(movies_id_ratings[movie_id])
        # Only update if there is a higher average than there is
        if(avg_movie_ratings > result[1]):
            # Update result with new maximum
            result = [movie_id, avg_movie_ratings]
    
    return result

def createListUsers(user_id, movies_ratings):
    # If already exists this movie_id
    if user_id in users_ratings:
        # Add new rating to the list of this movie_id
        users_ratings[user_id].append(movies_ratings)
    # If this origin does not yet exist    
    else:
        # Create two new rating list with movies_id like index
        users_ratings[user_id] = []
        # Add the first rating to the lists
        users_ratings[user_id].append(movies_ratings)

# List of users with min_times occurrences
def userLowestAvgRating(min_times):
    list_users_avg_ratings = [] # List created to get a specific ranking
    # Calculation of ratings averages for each user_id
    # Storing averages in a list along with your ID 
    for user_id in users_ratings.keys():    
        times = len(users_ratings[user_id])
        # Only add if its number of occurrences is greater than or equal to min_times
        if(times >= min_times):
            avg_user_ratings = sum(users_ratings[user_id])*1.0 / times
            # Add new user_id along with your número de apariciones and average to the list 
            list_users_avg_ratings.append([user_id, times, avg_user_ratings])
            
    return list_users_avg_ratings

def createListsGnresRatings(movies_id, movies_ratings, id_tit, gnres):
    # If gnres isn't trash 
    if gnres != "-1":
        gnres = gnres.split('|')
        # If yet exists this movie_id
        if id_tit not in movies_id_gnres:
            # Add new title to the lists with id_tit like index
            movies_id_gnres[id_tit] = gnres            
    # If movies_id isn't trash     
    elif movies_id != -1:    
        # If already exists this movie_id
        if movies_id in movies_id_ratings:
            # Add new rating to the list of this movie_id
            movies_id_ratings[movies_id].append(movies_ratings)
        # If this origin does not yet exist    
        else:
            # Create two new rating list with movies_id like index
            movies_id_ratings[movies_id] = []
            # Add the first rating to the lists
            movies_id_ratings[movies_id].append(movies_ratings)

def highestAvgRatedMovGenre():
    maxi = 0
    result = "-1"
    listGenres = {}
    # Calculation of ratings averages for each genre
    for movie_id in movies_id_ratings.keys():    
        avg_movie_ratings = sum(movies_id_ratings[movie_id])*1.0 / len(movies_id_ratings[movie_id])
        # Go down the gnre list of each movie
        for i in movies_id_gnres[movie_id]:
            # If it does not exist the genre is created with a new value, if it does not exist it is updated
            if i in listGenres:              
                listGenres[i] = (listGenres[i] + avg_movie_ratings)/2    
            else:  
                listGenres[i] = avg_movie_ratings
    # Go down the gnre list to find max average rating         
    for i in listGenres:
        if(listGenres[i] > maxi):
            maxi = listGenres[i]
            result = [i, maxi]    
    return result

# -------------------- Inputs processing -----------------------------
for line in sys.stdin:
    line = line.strip()
    movies_id, movies_ratings, id_tit, title, user_id, gnres = line.split('\t')
    # Convert inputs to numeric values
    movies_id = int(movies_id)
    movies_ratings = float(movies_ratings)
    id_tit = int(id_tit)
    user_id = int(user_id)
    
    # Create the corresponding lists and then find 
    # a movie according to your ratings (for PART 1)
    createListsMovRatings(movies_id, movies_ratings, id_tit, title)
      
    # Create the corresponding lists and then find 
    # a user according to your ratings (for PART 2)
    if user_id != -1:
        createListUsers(user_id, movies_ratings)

    # Create the corresponding lists and then find 
    # a gnre according to movies ratings (for PART 3)
    createListsGnresRatings(movies_id, movies_ratings, id_tit, gnres)
#  
# ---------------- PART 1 (Exercise 3) ------------
#
list_avg_movies_ratings = movieMaxAvgRating()
  
if(len(list_avg_movies_ratings)>0):
    print("\n__Movie title which has the maximum average rating__")
    id_best = list_avg_movies_ratings[0]
    print("TITLE\tMOVIE_ID\tAVG_MOVIE_RATING")
    print("{}\t{}\t{}".format(movies_id_title[id_best], id_best,round(list_avg_movies_ratings[1], 3)))
#
# ---------------- END PART 1 (Exercise 3) ------------ 
#

#  
# ---------------- PART 2 (Exercise 3) ------------
#
# 
min_times = 40
list_users_avg_ratings = userLowestAvgRating(min_times)
  
if(len(list_users_avg_ratings)>0):
    # Sort the list based on the ratings average
    list_users_avg_ratings.sort(key=lambda arr: arr[2])
      
    print("\n__User who has assign lowest average rating among all the users who rated more than {} times__".format(min_times))
    id_best = list_users_avg_ratings[0][0]
    times_best = list_users_avg_ratings[0][1]
    avg_user_ratings = round(list_users_avg_ratings[0][2], 3)
    print("USER_ID\tTIMES\tAVG_USER_RATING")
    print("{}\t{}\t{}".format(id_best, times_best, avg_user_ratings))    

#
# ---------------- END PART 2 (Exercise 3) ------------ 
#

#  
# ---------------- PART 3 (Exercise 3) ------------
#
print("\n__Find the highest average rated movie genre__")
par3 = highestAvgRatedMovGenre()
print("GNRE\tAVG_GNR_RATING")
print("{}\t{}".format(par3[0], round(par3[1],3))) 

#
# ---------------- END PART 3 (Exercise 3) ------------ 
#
