n, m = map(int,input().split())
points = list(map(int,input().split()))
solves = list(map(int,input().split()))
ans = 0

for q in solves:
  ans += points[q - 1]

print(ans)