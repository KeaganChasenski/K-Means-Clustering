import numpy as np
import matplotlib.pyplot as plt

#  Data (examples have two attributes: X, Y , both in range: [1, 10]).
data = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])

#params set by assignment brief
k = 3
centroids = np.array([[2,10],[5,8],[1,2]])  

def inital_data_graph():
    plt.scatter(data[:,0], data[:,1], label = "data points")
    plt.scatter(centroids[:,0], centroids[:,1], marker="x", label = "centroids")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Inital data points')
    plt.legend()
    plt.savefig('graphs/initial_data.png')


if __name__ == "__main__" :
    print("Ran from main")
    counter = 1 
    for i in data:
        print("example ", counter , ":" , i)
        counter += 1 
    inital_data_graph() 
