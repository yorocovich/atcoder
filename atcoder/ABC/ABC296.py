# A
n = int(input())
s = input()
x = 0
for i in range(1,n):
  if s[i-1] == "M" and s[i] == "F":
    continue
  if s[i-1] == "F" and s[i] == "M":
    continue
  else:
    print("No")
    exit()

print("Yes")

# B
borads = []
for _ in range(8):
  borads.append(list(input()))

for i in range(8):
  for j in range(8):
    if borads[i][j] == "*":
      v = str(8 - i)
      h = chr(96 + j + 1)
      print(h+v)

    