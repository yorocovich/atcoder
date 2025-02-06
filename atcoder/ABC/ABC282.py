# A
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
ans = alphabet[0:n]

print(ans)

# B
n, m = map(int,input().split())
result = []
for i in range(n):
  result.append(input())

ans = 0
for i in range(n):
  for j in range(i+1,n):
    ok = True
    for k in range(m):
      if result[i][k] == "x" and result[j][k] == "x":
        ok = False

    if ok:
      ans += 1

print(ans)