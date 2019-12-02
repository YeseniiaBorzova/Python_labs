n = int(input())
a = [[abs(i-j) for i in range(n)]for j in range(n)]
for row in a:
      print(' '.join([str(elem) for elem in row]))