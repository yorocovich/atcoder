# A
n, h, x = map(int,input().split())
pots = list(map(int,input().split()))

for i in range(n):
  if h + pots[i] >= x:
    print(i+1)
    break

# B
n = int(input())
nums = list(map(int,input().split()))

nums.sort()

for i in range(1,n):
  if nums[i-1] + 1 != nums[i]:
    print(nums[i-1]+1)
    break
