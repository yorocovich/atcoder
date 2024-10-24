x, y = map(int,input().split())

if x < y <= x+2 or x-3 <= y < x:
  print("Yes")
else:
  print("No")