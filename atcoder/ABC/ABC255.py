i, j = map(int,input().split())
a = []
for _ in range(2):
  a.append(list(map(int,input().split())))

print(a[i-1][j-1])