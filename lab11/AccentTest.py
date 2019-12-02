n = int(input())
accent = {}
for i in range(n):
    word = input()
    base = word.lower()
    if base not in accent:
        accent[base] = set()
    accent[base].add(word)

str = input().split()
mistakes = 0
for word in str:
    if((word.lower() in accent and word not in accent[word.lower()])
        or len([l for l in word if l.isupper()]) != 1):
        mistakes += 1

print(mistakes)