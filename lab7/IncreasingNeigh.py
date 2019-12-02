s = input()
a = s.split()
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        print(int(a[i]))