import collections

import numpy as np
from collections import OrderedDict

def run_length_encoding_np(arr):
    dict = collections.Counter(arr)
    return np.array(dict.keys()), np.array(dict.values());

def run_length_encoding_vec(arr):
    numbers = list(OrderedDict.fromkeys(arr))
    repeats = [list(arr).count(elem) for elem in numbers]
    return np.array(numbers), np.array(repeats)

def run_length_encoding_nonvec(arr):
    numbers = set(arr)
    repeats = list()
    for i in numbers:
        repeats.append(np.count_nonzero(arr == i))
    return np.array(numbers), np.array(repeats)

arr = np.random.randint(0,5, 6)
print('arr: ', arr)
print(run_length_encoding_np(arr))
print(run_length_encoding_vec(arr))
print(run_length_encoding_nonvec(arr))
