n = int(input())
nums = list(map(int,input().split()))

check = []
for num in nums:
  if num not in check:
    check.append(num)

check.sort()

print(check[-2])