n = int(input())
s = input()

a = 0
t = 0
f = False
for i in range(n):
  if s[i] == "A":
    a += 1
  else:
    t += 1
  
  if a >= n / 2:
    print("A")
    f = True
    break
  elif t >= n / 2:
    print("T")
    f = True
    break

if not f:
  print("A" if a > t else "T")