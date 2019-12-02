n = int(input())
j,t=n-1,int((n-1)/2)
a = [['.']*t+['*']+['.']*t for i in range(n)]
a[t]=['*']*n
for i in range(n):
    a[i][i]='*'
    a[j][i]='*'
    j-=1
for row in a:
    print(' '.join([str(elem) for elem in row]))