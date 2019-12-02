a = input().split()
m  = 0
for i in range(1,len(a)-1):
    if (int(a[i])>int(a[i-1])) and (int(a[i])>int(a[i+1])):
        m+=1
print(m)