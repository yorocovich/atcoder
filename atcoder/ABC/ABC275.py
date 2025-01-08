n = int(input())
t = list(map(int,input().split()))
ans = 0
t_num = 0

for i in range(n):
  if t_num < t[i]:
    t_num = t[i]
    ans = i + 1

print(ans)