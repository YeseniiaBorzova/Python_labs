max = 0
elem = -1
num=0
while elem!=0:
    elem = int(input())
    if elem>max:
        max,num = elem,1
    elif elem==max:
        num+=1
print(num)