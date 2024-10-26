m = []
ans = 0
for _ in range(8):
  m.append(input())

ng_i = []
ng_j = []
for i in range(8):
  for j in range(8):
    if m[i][j] == "#":
      ng_i.append(i)
      ng_j.append(j)

for i in range(8):
  if i in ng_i:
    continue

  for j in range(8):
    if j in ng_j:
      continue
    else:
      ans += 1

print(ans)
