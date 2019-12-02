n = int(input())
a = {}
max = 0
for i in range(n):
    line = input().split()
    for word in line:
        if word in a:
            a[word] += 1
        else:
            a[word] = 1
for x, y in a.items():
    if max < y:
        max = y
res = list()
for x, y in a.items():
    if y == max:
        res.append(x)
print(sorted(res)[0])
