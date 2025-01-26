x, y, n = map(int,input().split())
ans = 0

if x * 3 > y:
  ans = (n // 3) * y + (n % 3) * x
else:
  ans = n * x

print(ans)