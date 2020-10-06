import numpy as np
x = np.array([[4,3,7,13,-3],
           [2,5,-6,21,8],
           [-1,5,9,3,11],
           [9,-4,6,44,1]])
print("Initial \n",x)
x[1,:] = 0
print("Replaced zeros \n",x)
print("Reshaped \n",x.reshape(5,4))