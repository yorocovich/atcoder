# A
n = int(input())
s = input()
chk = 0
for i in range(n):
  if s[i] == "A":
    chk |= 1
  elif s[i] == "B":
    chk |= 2
  else:
    chk |= 4
  if chk & 7 == 7:
    print(i+1)
    break

# B
n, d = map(int,input().split())
strs = []
for _ in range(n):
  strs.append(input())

ans = 0
temp = 0
for i in range(d):
  is_free = ""
  for j in range(n):
    is_free += strs[j][i]
  if "x" not in is_free:
    temp += 1
  else:
    ans = max(ans,temp)
    temp = 0

ans = max(ans,temp)
print(ans)