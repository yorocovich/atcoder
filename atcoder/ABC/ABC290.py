# A
n, m = map(int,input().split())
points = list(map(int,input().split()))
solves = list(map(int,input().split()))
ans = 0

for q in solves:
  ans += points[q - 1]

print(ans)

# B
n, k = map(int,input().split())
s = input()
ans = ""
chk = 0
for i in range(n):
  if s[i] == "o" and chk < k:
    chk += 1
    ans += s[i]
  else:
    ans += "x"

print(ans)