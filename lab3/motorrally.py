import math
n = int(input())
m = int(input())
if m <= n:
    print(1)
else:
    print(math.ceil(m / n))