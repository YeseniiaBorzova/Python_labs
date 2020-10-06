import numpy as np
from functools import reduce

def npCalcSecTask(matr, i, j):
    vec = np.array([matr[i[k], j[k]] for k in range(len(i))])
    return vec

def vectorCalcSecTask(matr, i, j):
    vec = [matr[i[k], j[k]] for k in range(len(i))]
    return vec

def calcSecTask(matr, i, j):
    vec = []
    for k in range(len(i)):
        vec.append(matr[i[k], j[k]])
    return vec


n, m = input("Enter size(n m) of matrix: ").split()
n = int(n)
m = int(m)
matrix = np.random.randint(0, 15, (n, m))
i = np.random.randint(0,n - 1,n)
j = np.random.randint(0,m - 1,n)
print(i)
print(j)
print(matrix)
print(np.array_str(npCalcSecTask(matrix, i, j)))
print(vectorCalcSecTask(matrix, i, j))
print(calcSecTask(matrix, i, j))