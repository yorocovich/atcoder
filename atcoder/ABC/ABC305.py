n = int(input())

x = n // 5

if n % 5 in (0,1,2):
  print(x * 5)
else:
  print(x * 5 + 5)