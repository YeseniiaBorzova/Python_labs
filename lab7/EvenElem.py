s = input()
a = s.split()
for elem in a:
    if int(elem)%2==0:
        print(elem)