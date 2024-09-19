n = int(input())
nums = list(map(int,input().split()))
max_num = second_num = 0
max_pos = second_pos = 0
for i in range(len(nums)):
  if nums[i] > max_num:
    if max_num != 0:
      second_num = max_num
      second_pos = max_pos
    max_num = nums[i]
    max_pos = i + 1
  elif nums[i] > second_num:
    second_num = nums[i]
    second_pos = i + 1

print(second_pos)
    