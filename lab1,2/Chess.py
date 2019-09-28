row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())
if ((row1 + col1) % 2 == 0) and ((row2 + col2) % 2 == 0):
    print("YES")
elif ((row1 + col1) % 2 == 1) and ((row2 + col2) % 2 == 1):
    print("YES")
else:
    print("NO")
