n = int(input())
d = dict()
for i in range(n):
    arr = input().split()
    for i in range(1, len(arr)):
        d[arr[i]] = arr[0]

n = int(input())
for i in range(n):
    town = input()
    print(d[town])