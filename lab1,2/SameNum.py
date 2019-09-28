a = int(input())
b = int(input())
c = int(input())
if a!=b and a!=c and c!=b:
    print(0)
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print(2)
elif c==b and c==a and b==a:
    print(3)