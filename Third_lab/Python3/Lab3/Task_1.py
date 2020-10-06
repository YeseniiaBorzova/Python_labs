import numpy as np
from functools import reduce
import time

def npCalcDiagProd(matr):
    D = [matr[i, i] for i in range(min(matr.shape[0], matr.shape[1])) if matr[i, i] != 0]
    return np.multiply.reduce(D)

def vectorCalcDiagProd(matr):
    D = [matr[i, i] for i in range(min(matr.shape[0], matr.shape[1])) if matr[i, i] != 0]
    return reduce(lambda x, y: x*y, D)

def calcDiagProd(matr):
    prod = 1
    for i in range(min(matr.shape[0], matr.shape[1])):
        if matr[i, i] != 0:
            prod *= matr[i, i]
    return prod


n, m = input("Enter size(n m) of matrix: ").split()
n = int(n)
m = int(m)
matrix = np.random.randint(0, 15, (n, m))
print(matrix)
print(npCalcDiagProd(matrix))
print(vectorCalcDiagProd(matrix))
print(calcDiagProd(matrix))