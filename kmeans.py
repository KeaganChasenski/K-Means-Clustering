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
centroids = {'1':X[0] , '2':X[3], '3':X[6] }

colors = 10*["g","r","c","b","k"]

def inital_data_graph():  
    plt.scatter(X[:,0], X[:,1], label = "data points")
    plt.scatter(centroids[:,0], centroids[:,1], marker="x", label = "centroids")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Inital data points')
    plt.legend()
    plt.savefig('graphs/initial_data.png')

def kmeans():
    # for loop to stop infinite loop
    for i in range(max_itterations):
        print('Iteration ', i+1 )
        classifications = {}

        # loop creates 3 clusters
        for i in range(k):
            classifications[i] = []

        # Loop for each set of coordinates in data points
        for set in X:
            distances = [distance(set, centroids[centroid]) for centroid in centroids]
            classification = distances.index(min(distances))
            #print(classification)
            classifications[classification].append(set)
        print(centroids)
        print(classifications)

        # Compare previous s=centriods 
        prev_centroids = copy.deepcopy(centroids)

        for classification in classifications:
            centroids[classification] = np.average(classifications[classification],axis=0)
            
        optimzed = True

        for c in centroids:
            print(c)
            orginal_centriods = prev_centroids[c+1 + '']
            current_centriod = centroids[c]

            if np.sum((current_centriod - orginal_centriods) / orginal_centriods * 100) > tolerance:
                optimzed = False 
        
        if optimzed:
            break 

def distance(p1, p2):
    distance = math.sqrt( ( (p1[0]-p2[0]) **2)  + ( (p1[1]-p2[1]) **2) )
    return distance


if __name__ == "__main__" :
    #print("Ran from main")
    #counter = 1 
    #for i in data:
        #print("example ", counter , ":" , i)
        #counter += 1 
    #inital_data_graph() 
    kmeans()
    