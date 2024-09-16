n = int(input())

a = []
for _ in range(n):
  a.append(list(map(int, input().split())))

j = 0
for i in range(n):
  if j > i:
    j = a[j][i] - 1
  else:
    j = a[i][j] - 1

print(j + 1)
