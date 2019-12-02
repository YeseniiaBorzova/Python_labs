def power(a,n):
    res = 1
    if n==0:
        return 1
    elif n>0:
        for i in range(n):
            res*=a
    elif n<0:
        for i in range(-n):
            res*=(1/a)
    return res
a = float(input())
n = int(input())
print(power(a,n))