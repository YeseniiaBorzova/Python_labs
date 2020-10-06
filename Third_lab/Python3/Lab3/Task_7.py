import numpy as np
from scipy.spatial import distance

def euclidean_distance_nonvec(x, y):
    matrix = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            matrix[i, j] = np.linalg.norm(x[i] - y[j])
    return matrix

def euclidean_distance_np(x, y):
    return distance.cdist(x, y, 'euclidean')

def euclidean_distance_vec(x, y):
    matrix = np.array(
        [[np.linalg.norm(a_elem - b_elem)
          for b_elem in y] for a_elem in x])
    return matrix

x = np.array([[0, 0, 0],
              [0, 0, 1],
              [0, 1, 0],
              [0, 1, 1],
              [1, 0, 0],
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 1]])
y = np.array([[0.1, 0.2, 0.4]])

print("Sample X:\n", x, "\nSample Y:\n", y)
print("\nVec:\n",euclidean_distance_vec(x, y).round(3))
print("\nNon_vec:\n",euclidean_distance_nonvec(x, y).round(3))
print("\nNP:\n",euclidean_distance_np(x, y).round(3))
