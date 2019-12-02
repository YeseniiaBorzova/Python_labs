i = 0
a = 1
max = -1
while a!=0:
    a = int(input())
    if a>=max:
        max=a
    if a==0:
        break
print(max)