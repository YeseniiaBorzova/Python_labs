a = input().split()
count=1
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        count+=1
print(count)