n = int(input())
a = {}
for i in range(n):
    file, *permission = input().split()
    a[file] = permission

m = int(input())
for i in range(m):
    permission, file = input().split()
    if permission == "read" and  "R" in a[file]:
        print("OK")
    elif permission == "write" and "W" in a[file]:
        print("OK")
    elif permission == "execute" and  "X" in a[file]:
        print("OK")
    else:
        print("Access denied")