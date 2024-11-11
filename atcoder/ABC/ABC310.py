n, p, q = map(int,input().split())
dishes = list(map(int,input().split()))
ans = 100001
for i in range(n):
  if dishes[i] < p - q:
    ans = min(ans,dishes[i] + q)

print(p if ans == 100001 else ans)