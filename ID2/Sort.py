import numpy as np

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_array = []
rand_arr = np.random.randint(0,100,20)
rand_arr_buble = np.random.randint(0,100,20)
bubbleSort(rand_arr_buble)
a = int(input("Size of array:"))
for i in range(a):
    my_array.append(int(input()))
my_array = np.array(my_array)
buble_array=np.array(my_array)
bubbleSort(buble_array)
my_array.sort()
rand_arr.sort()
print("Built in sort function: ",my_array)
print("Buble sort: ", buble_array)
print("Random created array sorted: ", rand_arr)
print("Random created array buble sorted: ", rand_arr_buble)