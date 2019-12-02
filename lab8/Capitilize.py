def capitilize(word):
    first = word[0]
    first = chr(ord(first)-32)
    return first+word[1:]

s = input().split()
result = []
for i in s:
    result.append(capitilize(i))
print(' '.join(result))