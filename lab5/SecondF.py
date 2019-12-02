s = input()
a = s.count('f')
p = s.find('f')
if a==1:
    print(-1)
elif a == 0:
    print(-2)
else:
    print(s.find('f',s.find('f')+1))