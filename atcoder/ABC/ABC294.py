# A
n = int(input())
nums = list(map(int,input().split()))

ans = []

for i in range(n):
  if nums[i] % 2 == 0:
    ans.append(nums[i])

print(*ans)

# B
h, w = map(int,input().split())
nums = []
for i in range(h):
  nums.append(list(map(int,input().split())))

ans_char = ''
ans = []
for j in range(h):
  for k in range(w):
    if nums[j][k] == 0:
        ans_char += '.'
    elif 1 <= nums[j][k] <= 26:
        ans_char += chr(64 + nums[j][k])
  ans.append(ans_char)
  ans_char = ''

for i in range(h):
  print(ans[i])
  