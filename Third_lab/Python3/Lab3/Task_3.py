import numpy as np
from collections import Counter

def checkMultiset(x, y):
    if len(x) != len(y):
        return False
    xdict = Counter(x)
    ydict = Counter(y)
    for key in xdict.keys():
        if xdict[key] != ydict[key]:
            return False
    return True

def checkMultisetNp(x,y):
    return np.array_equal(np.sort(x), np.sort(y))

def checkMultisetVec(x, y):
    if len(x) != len(y):
        return False
    x = np.sort(x)
    y = np.sort(y)
    res = [False for i in range (len(x)) if x[i] != y[i]  ]
    return not(False in res)

x = input().split()
y = input().split()
print(checkMultiset(x,y))
print(checkMultisetNp(x,y))
print(checkMultisetVec(x,y))