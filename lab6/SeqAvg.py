i = 0
a = 1
sum = 0
while a!=0:
    a = int(input())
    if a==0:
        break
    i+=1
    sum+=a
print(sum/i)