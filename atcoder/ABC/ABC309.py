a, b = map(int,input().split())

if a not in (3,6,9) and b-a == 1:
  print("Yes")
else:
  print("No")