n = int(input())
a = set()
b = [[str(j) for j in input().split(' ')] for i in range(n)]
for i in range(len(b)):
    for j in range(len(b[i])):
        a.add(b[i][j])
print(len(a))