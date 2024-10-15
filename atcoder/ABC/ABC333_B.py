s1s2 = input()
t1t2 = input()

len1 = ("AC","AD","BD","BE","CE")
len2 = ("AB","AE","BC","CD","DE")

s1s2 = ''.join(sorted(s1s2))
t1t2 = ''.join(sorted(t1t2))

if s1s2 in len1 and t1t2 in len1:
  print("Yes")
elif s1s2 in len2 and t1t2 in len2:
  print("Yes")
else:
  print("No")