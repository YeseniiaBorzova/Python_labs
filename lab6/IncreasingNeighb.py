a=-1
i=-1
while a!=0:
    prev=a
    a = int(input())
    current = a
    if current>prev:
        i+=1
    prev = current
print(i)