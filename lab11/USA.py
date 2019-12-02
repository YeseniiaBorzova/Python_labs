d = dict()
for i in range(int(input())):
    s1, s2 = input().split()
    if s1 in d:
        d[s1] += int(s2)
    else:
        d[s1] = int(s2)

for s in sorted(d):
    print(s, d[s])