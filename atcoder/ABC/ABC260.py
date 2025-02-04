s = input()
c1 = s[0]
c2 = s[1]
c3 = s[2]

if c1 == c2 == c3:
  print("-1")
elif c1 == c2:
  print(c3)
elif c2 == c3:
  print(c1)
elif c3 == c1:
  print(c2)
else:
  print(c1)