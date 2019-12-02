a = [ int(i) for i in input().split() ]
index_Max = a.index(max(a))
index_Min=a.index(min(a))
Max = max(a)
Min = min(a)
a[index_Max] = Min
a[index_Min] = Max
print(' '.join([str(i) for i in a]))
