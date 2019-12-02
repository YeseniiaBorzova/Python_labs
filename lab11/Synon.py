d = dict()
for i in range(int(input())):
    s1, s2 = input().split()
    d[s1] = s2

res = input()

if res in d:
    print(d[res])
else:
    for key, value in d.items():
        if value == res:
            print(key)