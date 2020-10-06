import numpy as np

def maxBeforeZeroNP(arr):
    res = [arr[i] for i in range(1, len(arr)) if arr[i - 1] == 0]
    res.sort()
    return res[-1]

def maxBeforeZeroVec(arr):
    return max([arr[i] for i in range(1, len(arr)) if arr[i - 1] == 0])

def maxBeforeZero(arr):
    max = min(arr)
    for i in range(1, len(arr)):
        if arr[i - 1] == 0 and max < arr[i]:
            max = arr[i]
    return max

arr = np.array([int(x) for x in input().split()])
print(maxBeforeZero(arr))
print(maxBeforeZeroNP(arr))
print(maxBeforeZeroVec(arr))