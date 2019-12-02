from collections import Counter

n = int(input())
d = dict()
for i in range(n):
    for word in input().split():
        if word in d:
            d[word]+=1
        else:
            d[word] = 1

counter = Counter(d)

pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]

print('\n'.join(words))