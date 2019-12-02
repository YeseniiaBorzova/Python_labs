a = input().split()
m  = 0
for i in range(1,len(a)):
    if (int(a[i])>=0) and (int(a[i-1])>=0):
        m+=1
        print(a[i-1],a[i])
        if m==1:
            break
    elif (int(a[i])<0) and (int(a[i-1])<0):
        m+=1
        print(a[i-1],a[i])
        if m ==1:
            break