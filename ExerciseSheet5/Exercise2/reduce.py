'''
Created on 16 may. 2017

@author: Mario Rodriguez
'''
import sys

origin_dep_delay = {}
origin_arr_delay = {}
max_dep_delay = {}
min_dep_delay = {}

# Classification of airports
for line in sys.stdin:
    line = line.strip()
    origin, dep_delay, arr_delay = line.split('\t')
    dep_delay = float(dep_delay)
    arr_delay = float(arr_delay)
    
    # If already exists this origin
    if origin in origin_dep_delay:
        # Add new items to the lists
        origin_dep_delay[origin].append(dep_delay)
        origin_arr_delay[origin].append(arr_delay)
        # Need to update the maximum?
        if dep_delay > max_dep_delay[origin]:
            max_dep_delay[origin] = dep_delay
        # Need to update the minimum?
        if dep_delay < min_dep_delay[origin]:
            min_dep_delay[origin] = dep_delay
    # If this origin does not yet exist    
    else:
        # Create two new list
        origin_dep_delay[origin] = []
        origin_arr_delay[origin] = []
        # Add the first items to the lists
        origin_dep_delay[origin].append(dep_delay)
        origin_arr_delay[origin].append(arr_delay)
        # Initial value of the maximum and minimum
        max_dep_delay[origin] = dep_delay
        min_dep_delay[origin] = dep_delay

# Airports reduce
list_arr_delay = [] # List created to get a specific ranking
print("ORIGIN\tMAX_DEP_DELAY\tMIN_DEP_DELAY\tAVG_DEP_DELAY\tAVG_ARR_DELAY")
for origin in origin_dep_delay.keys():
    # Calculation of averages
    avg_dep_delay = sum(origin_dep_delay[origin])*1.0 / len(origin_dep_delay[origin])
    avg_arr_delay = sum(origin_arr_delay[origin])*1.0 / len(origin_arr_delay[origin])
    # Add new items to the list 
    list_arr_delay.append([origin, avg_arr_delay])
    print ("{}\t{}\t{}\t{}\t{}".format(origin, max_dep_delay[origin], min_dep_delay[origin], round(avg_dep_delay, 3), round(avg_arr_delay, 3)))

# List top 10 airports
list_arr_delay.sort(key=lambda arr: arr[1])
print("\n__Ranking list that contains top 10 airports by their average arrival delay__")
print("ORIGIN\tAVG_ARR_DELAY")
for i in range(10):
    print("{}\t{}".format(list_arr_delay[i][0], round(list_arr_delay[i][1], 3)))

# List of the 10 worst airports
print("\n__Ranking list that contains worst 10 airports by their average arrival delay__")
print("ORIGIN\tAVG_ARR_DELAY")
for i in range(len(list_arr_delay)-1, len(list_arr_delay)-11, -1):
    print("{}\t{}".format(list_arr_delay[i][0], round(list_arr_delay[i][1], 3)))
