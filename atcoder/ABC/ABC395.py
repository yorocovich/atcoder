n = int(input())
nums = list(map(int,input().split()))

for i in range(1,n):
  if nums[i] <= nums[i-1]:
    print("No")
    exit()

print("Yes")