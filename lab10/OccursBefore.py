a = [int(i) for i in input().split()]
c = set()
for i in range(len(a)):
    if a[i] in c:
        print("YES")
    else:
        print("NO")
    c.add(a[i])