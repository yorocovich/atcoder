n, a, b = map(int, input().split())
res = 0
for x in range(1, n + 1):
  d = 0
  for y in str(x):
    d += int(y)
  if a <= d <= b:
    res += x

print(res)

