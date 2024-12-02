# A
nums = map(int,input().split())
before = 0
is_ok = True
for num in nums:
  if num % 25 != 0 or 100 > num or num > 675 or num < before:
    is_ok = False
    break
  before = num

print('Yes' if is_ok else 'No')

# B
n, m = map(int,input().split())
colors = list(input().split())
dishes = list(input().split())
prices = list(map(int,input().split()))
ans = 0
for i in range(n):
  ans += prices[dishes.index(colors[i]) + 1 if colors[i] in dishes else 0]

print(ans)