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


def distance(p1,p2):
    distance = math.sqrt( ( (p1[0]-p2[0]) **2)  + ( (p1[1]-p2[1]) **2) )
    return distance

def kmeans():
    for i in range(max_itterations):
        print('Itteration ', i+1, '\n')
        clusters = {}

        for i in range(k):
            clusters[i] = []

        ###### Step 2 - Calculate Distance for each data point to each centriod ######
        for x in X:
            distances = [distance(x, centroids[i]) for i in centroids.keys()]

            ###### Step 3 - Assign each data point to nearest centriod ######
            cluster = distances.index(min(distances))
            clusters[cluster].append(x)

        for i in clusters.keys():           
            print('Cluster ', i+1, ':' , clusters[i])
            print('Centriod: ', centroids[i+1] ,"\n")
        
        ##### Step 4 - calculate new centroids from mean of cluster ######
        # Deep copy of centroids made so can compare
        prev_centroids = copy.deepcopy(centroids)
        

        # Calculate the new average of each cluster
        for c in clusters.keys():
            print('cluster at c')
            print(clusters[c])
            centroids[c+1] = np.mean(clusters[c], axis=0, dtype=np.float16)


        ##### Step 5 - Reassign clusters based on new centroids ######
        optimized = True

        for c in centroids:
            original_centroid = prev_centroids[c]
            current_centroid = centroids[c]
            
            if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > tolerance:
                optimized = False 

        if optimized:
            break

        ##### Step 6 - repeate 4 and 5 until done. ######
        ##### Done above in for loop of max itterations #####

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
    colors = map(lambda x: colmap[x+1], labels)
    plt.scatter(X[:,0], X[:,1], color = colors, label = "data points")

    colmap = {1: 'r', 2: 'g', 3: 'b'}
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Clustered data points')
    plt.legend()
    plt.savefig('graphs/clustered_data.png')

if __name__ == "__main__" :  

    inital_data_graph()
    ##### Step 1 - Assign starting centriods ######
    #### done in params above #####
    kmeans()
    clustered_data_graph()
    


        
    