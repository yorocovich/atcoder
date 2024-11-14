n = int(input())
steps = list(map(int,input().split()))
ans = []
step = 0

for i in range(1,len(steps)+1):
  step += steps[i-1]
  if i % 7 == 0:
    ans.append(step)
    step = 0

print(*ans)