import numpy as np
height = np.array([68,71,72,75,75,75,68,74,78,71])
weight = np.array([155,185,185,200,225,225,220,160,205,235])
height = height/39.37
weight = weight/2.205
bmi = weight/(height*height)
print("All indexies: \n",bmi)
print("BMI < 21: ",bmi[bmi<21])

