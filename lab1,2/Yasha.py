N = int(input())
M = int(input())
x = int(input())
y = int(input())
min = x
if 0<=y<min:
    min=y
if 0<=M-x<min:
    min=M-x
if 0<=N-y<min:
    min=N-y
print(min)