import numpy as np
import matplotlib.pyplot as plt

#  Data (examples have two attributes: X, Y , both in range: [1, 10]).
data = [[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]

if __name__ == "__main__" :
    print("Ran from main")
    counter = 1 
    for i in data:
        print("example ", counter , ":" , i)
        counter += 1 

