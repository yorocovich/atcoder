n, k = map(int,input().split())
nums = list(map(int,input().split()))

for i in range(k):
  nums.pop(0)
  nums.append(0)

print(*nums)