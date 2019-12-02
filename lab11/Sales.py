from collections import defaultdict

d = defaultdict(lambda: defaultdict(int))

for i in range (6):
    surn, item, num = input().split()
    d[surn][item] += int(num)

for client in sorted(d):
    print(client + ':')
    for thing in sorted(d[client]):
        print(thing, d[client][thing])