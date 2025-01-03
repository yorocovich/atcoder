s = input()
ans = 0
for i in range(len(s)):
  if s[i] == "v":
    ans += 1
  elif s[i] == "w":
    ans += 2
  else:
    ans += 0

print(ans)