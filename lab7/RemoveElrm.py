a = [ int(i) for i in input().split() ]
k = int(input())
for i in range(k+1,len(a)):
    a[i-1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))