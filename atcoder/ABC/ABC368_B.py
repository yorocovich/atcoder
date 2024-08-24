n = int(input())
nums = [int(_) for _ in input().split()]
res = 0

while True:
  temp = []
  for a in nums:
    if a > 0:
      temp.append(a)
  if len(temp) <= 1:
    break
  else:
    nums = temp

  nums = sorted(nums,reverse=True)

  nums[0] -= 1
  nums[1] -= 1

  res += 1

print(res)
