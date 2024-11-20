# A
n = input()
a = b = c = 0

for i in range(6):
  if n[i] == '1':
    a += 1
  elif n[i] == '2':
    b += 1
  elif n[i] == '3':
    c += 1
    
if a == 1 and b == 2 and c == 3:
  print('Yes')
else:
  print('No')

# B
s = input()
cnt = 0
ans = []
for i in range(len(s)):
  if s[i] == "|":
    if cnt > 0:
      ans.append(cnt)
      cnt = 0
    continue
  else:
    cnt += 1

print(*ans)