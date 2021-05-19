import numpy as np
import matplotlib.pyplot as plt
import math
import copy

# Data (examples have two attributes: X, Y , both in range: [1, 10]).
X = [[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]
X_elements = {1:[2,10],2:[2,5],3:[8,4],4:[5,8],5:[7,5],6:[6,4],7:[1,2],8:[4,9]}

# Hyperparamters
tolerance = 0.001
max_itterations = 10

# params set by assignment brief
k = 3

##### Step 1 - Assign starting centriods ######
centroids = {1:[2,10] , 2:[5,8], 3:[1,2]}

def distance(p1,p2):
    # Simple function to calculate Euclidean distance of two points
    # Returns distance 
    distance = math.sqrt( ( (p1[0]-p2[0]) **2)  + ( (p1[1]-p2[1]) **2) )
    return distance

def optimised(prev_centroids):
    # Loop through each centroid value 
    for c in centroids:
        # Assign previous and current centroids
        original_centroid = prev_centroids[c]
        current_centroid = centroids[c]

        # Check to see that the percentage change is greater than the hyperparamter tolerance
        # If it is greater return optimised = False to allow looping to next itteration    
        if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > tolerance:
            return  False 
    
    return True

def get_key(val):
    # Code used to search the dictionary of X_elements and output the key when the 2D array element is found
    for key, value in X_elements.items():
         if val == value:
            return key
 
    return "error 404"

def print_output(clusters):
    # Loop through keys in clusters array (1,2,3) 
    for i in clusters.keys(): 

        # Some additional code to be able to print element number instead of the array value in X
        items = clusters[i]
        elements = []
        for c in items:
            elements.append(get_key(c))

        converted_list = [str(element) for element in elements]
        elements_string = ", ".join(converted_list)

        cent = centroids[i+1]
        round_centroids = [round(num, 3) for num in cent]
        round_centroids = [str(rc) for rc in round_centroids]
        centroids_string = ", ".join(round_centroids)
        centroids_string = "(" + centroids_string + ")"

        print('Cluster ', i+1, ':' , elements_string)
        print('Centriod: ',centroids_string ," \n")

def kmeans():
    ##### Loop for each itteration of kmeans() #####

    for i in range(max_itterations):
        print('Itteration ', i+1, '\n')
        clusters = {}

        # Create K number of cluster arrays
        for i in range(k):
            clusters[i] = []

        ###### Step 2 - Calculate Distance for each data point to each centriod ######
        for x in X:
            distances = [distance(x, centroids[i]) for i in centroids.keys()]

            ###### Step 3 - Assign each data point to nearest centriod ######
            cluster = distances.index(min(distances))
            clusters[cluster].append(x)

        # Output Cluster and their associated data points as well as centroids
        print_output(clusters)
        
        # Deep copy of centroids made so can compare
        prev_centroids = copy.deepcopy(centroids)

        ##### Step 4 - calculate new centroids from mean of cluster ######
        
        # Calculate the new average of each cluster
        for c in clusters.keys():
            centroids[c+1] = np.mean(clusters[c], axis=0)

        ##### Step 5 - Reassign clusters based on new centroids ######
        ##### Done in next itteration of loop by clearing clusters {} #####

        ##### Step 6 - repeate 4 and 5 until max itterations reach or optimzed is True. ######
        if optimised(prev_centroids):
            break
 
def inital_data_graph():  
    plt.scatter(X[:,0], X[:,1], color = 'k', label = "data points")

    colmap = {1: 'r', 2: 'g', 3: 'b'}
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i] ,marker="x", label = "centroid %s" %i)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Inital data points')
    plt.legend()
    plt.savefig('graphs/initial_data.png')

def clustered_data_graph():
    plt.scatter(X[:,0], X[:,1],label = "data points")

    colmap = {1: 'r', 2: 'g', 3: 'b'}
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Clustered data points')
    plt.legend()
    plt.savefig('graphs/clustered_data.png')

if __name__ == "__main__" :  

    #inital_data_graph()

    ##### Step 2-6 - In kmeans() function ######
    kmeans()

    #clustered_data_graph()
    


        
    