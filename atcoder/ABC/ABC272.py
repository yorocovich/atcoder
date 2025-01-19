n = int(input())
nums = list(map(int,input().split()))
ans = 0
for i in range(n):
  ans += nums[i]
print(ans)