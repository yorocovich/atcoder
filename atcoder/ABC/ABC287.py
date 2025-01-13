# A
n = int(input())
f = a = 0
for _ in range(n):
  if input() == 'For':
    f += 1
  else:
    a += 1

print('Yes' if f > a else 'No')

# B
n, m = map(int,input().split())
nums = []
for i in range(n):
  s = input()
  nums.append(s[-3:])

nums2 = []
for i in range(m):
  nums2.append(input())

ans = 0
for chk in nums:
  if chk in nums2:
    ans += 1

print(ans)
