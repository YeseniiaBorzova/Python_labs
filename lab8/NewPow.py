def power(a,n):
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        return a*power(a,n-1)
a = float(input())
n = int(input())
print(power(a,n))