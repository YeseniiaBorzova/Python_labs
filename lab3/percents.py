import math
P = int(input())
X = int(input())
Y = int(input())
S = X*100+Y
percent = math.floor(S*(P/100))
S = S + percent
print(S//100,S%100)