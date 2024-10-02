s = input()

i = 1
ans = []
while i <= len(s):
  for j in range(len(s)-i+1):
    if s[j:j+i] in ans:
      continue
    else:
      ans.append(s[j:j+i])
  i += 1
print(len(ans))