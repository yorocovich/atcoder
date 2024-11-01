n, m, p = map(int,input().split())

if n - m < 0:
  print(0)
  exit()

print((n-m)//p+1)