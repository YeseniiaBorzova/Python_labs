a = input().split()
index = 0
for i in range(len(a)):
    a[i] = int(a[i])
    max = a[0]
for i in range(len(a)):
    if a[i]>max:
        max, index = a[i], i
print(max,index)