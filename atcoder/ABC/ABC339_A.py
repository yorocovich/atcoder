strs = input()
ans = ""
for i in range(len(strs)):
  if strs[i] == ".":
    ans = ""
  else:
    ans += strs[i]

print(ans)