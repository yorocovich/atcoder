n , y = map(int,input().split())
has_result = 0
for a in range(n + 1):
  if a * 10000 > y:
    has_result = -1
    break
  for b in range(n + 1 - a):
    c = n - a - b
    if a * 10000 + b * 5000 + c * 1000 == y:
      has_result = 1
      break
  if has_result != 0:
    break

print("-1 -1 -1" if has_result <= 0 else str(a)+chr(32)+str(b)+chr(32)+str(c))