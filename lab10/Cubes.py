a = [int(i) for i in input().split()]
n = a[0]
m = a[1]
set_Ann=set()
set_Borya=set()
for i in range(n):
    b = int(input())
    set_Ann.add(b)
for i in range(m):
    b = int(input())
    set_Borya.add(b)
print(len(set_Ann.intersection(set_Borya)))
print(' '.join(str(i) for i in (sorted(set_Ann.intersection(set_Borya)))))
print(len((set_Ann.symmetric_difference(set_Borya)).intersection(set_Ann)))
print(' '.join(str(i) for i in (sorted((set_Ann.symmetric_difference(set_Borya)).intersection(set_Ann)))))
print(len((set_Borya.symmetric_difference(set_Ann)).intersection(set_Borya)))
print(' '.join(str(i) for i in (sorted((set_Borya.symmetric_difference(set_Ann)).intersection(set_Borya)))))

