s = input()

out_str = s[0]

for i in range(1,len(s)):
  if s[i] != s[i-1]:
    out_str += s[i]

if out_str in ("","A","B","C","AB","BC","AC","ABC"):
  print("Yes")
else:
  print("No")