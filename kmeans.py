import numpy as np
import matplotlib.pyplot as plt
import math
import copy

# Data (examples have two attributes: X, Y , both in range: [1, 10]).
X = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])
cluster1 = []
cluster2 = []
cluster3 = []
# Hyperparamters
tolerance = 0.001
max_itterations = 10

# params set by assignment brief
k = 3
centroids = {1:[2,10] , 2: [5,8], 3:[1,2]}

if __name__ == "__main__" :  

    for x in X:
        distances = [np.linalg.norm(x-centroids[i]) for i in centroids.keys()]
        classification = distances.index(min(distances))
        print(classification)


        
    