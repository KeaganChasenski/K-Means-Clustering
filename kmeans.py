import numpy as np
import matplotlib.pyplot as plt
import math
import copy

# Data (examples have two attributes: X, Y , both in range: [1, 10]).
X = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])

# Hyperparamters
tolerance = 0.001
max_itterations = 10

# params set by assignment brief
k = 3
centroids = {1:[2,10] , 2: [5,8], 3:[1,2]}

def example_number(check):
    if check.all() == [2,10]:
        return 1
    elif check == [2,5]:
        return 2
    elif check == [8,4]:
        return 3
    elif check == [5,8]:
        return 4
    elif check == [7,5]:
        return 5
    elif check == [6,4]:
        return 6
    elif check == [1,2]:
        return 7
    else:
        return 8

def distance(p1,p2):
    distance = math.sqrt( ( (p1[0]-p2[0]) **2)  + ( (p1[1]-p2[1]) **2) )
    return distance

if __name__ == "__main__" :  
    ##### Step 1 - Assign starting centriods ######
    #### done in params above #####
    
    print('Itteration 1 \n')
    classifications = {}

    for i in range(k):
        classifications[i] = []

    ###### Step 2 - Calculate Distance for each data point to each centriod ######
    for x in X:
        distances = [distance(x, centroids[i]) for i in centroids.keys()]

        ###### Step 3 - Assign each data point to nearest centriod ######
        classification = distances.index(min(distances))
        classifications[classification].append(x)

    for i in classifications.keys():
        list = classifications[i]  
        
        print('Cluster ', i+1, ':' , list)
        print('Centriod: ', centroids[i+1] ,"\n")
    
    ##### Step 4 - calculate new centroids from mean of cluster ######
    # Deep copy of centroids made so can compare
    prev_centriods = copy.deepcopy(centroids)

    # Calculate the new average of each cluster
    for c in classifications.keys():
        print(np.average(classifications[c],axis=0))

    ##### Step 5 - Reassign clusters based on new centroids ######

    ##### Step 6 - repeate 4 and 5 until done. ######



        
    