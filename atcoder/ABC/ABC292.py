# A
s = input()
print(s.upper())

# B
n, q = map(int,input().split())

yellow = []
red = []
for i in range(q):
  c, x = map(int,input().split())
  if c == 1:
    if x in yellow:
      red.append(x)
      yellow.remove(x)
    else:
      yellow.append(x)
  elif c == 2:
    red.append(x)
  elif c == 3:
    if x in red:
      print("Yes")
    else:
      print("No")
