# A
nums = list(map(int,input().split()))
nums.sort()

if nums[0] * nums[1] == nums[2]:
  print("Yes")
else:
  print("No")

# B
n, m = map(int,input().split())
numbers = list(map(int,input().split()))
ans = []

for i in range(1,n+1):
  if i not in numbers:
    ans.append(i)

print(len(ans))
print(*ans)