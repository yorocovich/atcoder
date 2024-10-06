s = input()
t = input()
ans = 0
if s == t:
  print(0)
else:
  for i in range(min(len(s),len(t))):
    if s[i] != t[i]:
      ans = i + 1
      break
  
  if ans == 0:
    ans = min(len(s),len(t))+1

  print(ans)
  