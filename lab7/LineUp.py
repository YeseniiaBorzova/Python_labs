a = input().split()
height = int(input())
index = 1
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)):
    if height<=a[i]:
        index+=1
print(index)
