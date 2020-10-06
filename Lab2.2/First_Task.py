import numpy as np
info = np.array([[76,74,72,72,75,73,73,73,70,70,70,76,68,71,72,75,75,75,68,74],
                [190,220,180,205,210,220,211,200,180,190,170,230,155,185,185,200,225,225,220,160],
                [24.79,31.74,23.92,25.33,24.02,23.7,31.59,29.95,23.64,32.33,23.13,26.6,26.46,25.75,27.51,25.11,32.51,34.67,31.06,29.1]])
info[0,:] = info[0,:]/39.37
info[1,:] = info[1,:]/2.205
print("Information about 4th player: \n height: ",round(info[0][3],2),'m',"\n weight: ",round(info[1][3],3),"kg"," \n age: ",info[2][3],"years")
print("Weight of all players: ")
for i in range(len(info[1])):
    print(round(info[1][i],2),"kg")
index4=info[1][3]/(info[0][3]*info[0][3])
index6=info[1][5]/(info[0][5]*info[0][5])
if index4>index6:
    print("Mass index of the 4th player is bigger than 6th")
else:
    print("Mass index of the 6th player is bigger than 4th")

print("Information about 2nd and 3th players: ",info[0:2,1:3])
print("Shape:",info.shape,',',"Amount of elements:",info.size,',',"type: ",info.dtype)