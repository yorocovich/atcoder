# A
n = int(input())
words = list(input().split())

for word in words:
  if word in ("and", "not", "that", "the", "you"):
    print("Yes")
    exit()

print("No")

# B
r, c = map(int,input().split())
map_ori = []
for i in range(r):
  map_ori.append(list(input()))

for i in range(r):
  for j in range(c):
    if map_ori[i][j] not in (".","#"):
      L = int(map_ori[i][j])
      map_ori[i][j] = "."
      for k in range(r):
        for l in range(c):
          if (abs(i - k) + abs(l - j) <= L) and (not map_ori[k][l].isdigit()):
            map_ori[k][l] = "."

for x in map_ori:
  print("".join(x))