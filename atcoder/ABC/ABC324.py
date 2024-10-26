n = int(input())
nums = list(map(int,input().split()))

for i in range(1,n):
  if nums[i-1] != nums[i]:
    print("No")
    exit()

print("Yes")