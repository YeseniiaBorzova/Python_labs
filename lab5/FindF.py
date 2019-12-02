s = input()
a = s.count('f')
if a==1:
    print(s.find('f'))
elif a == 0:
    print(' ')
else:
    print(s.find('f'),s.rfind('f'))