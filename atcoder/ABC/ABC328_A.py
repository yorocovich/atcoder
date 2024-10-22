n, x = map(int,input().split())
points = list(map(int,input().split()))
ans = 0
for point in points:
  if point <= x:
    ans += point

print(ans)