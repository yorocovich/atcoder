x = input()
ans = ''
for i in range(len(x)):
  if x[i] in ('a','i','u','e','o'):
    continue
  else:
    ans += x[i]

print(ans)