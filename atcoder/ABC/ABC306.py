# A
n = int(input())
s = input()
ans = ""

for i in range(n):
  ans += s[i]*2

print(ans)

# B
nums = list(map(int,input().split()))
ans = 0

for i in range(64):
  ans += nums[i] * (2 ** i)

print(ans)