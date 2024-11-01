# A
n, m, p = map(int,input().split())

if n - m < 0:
  print(0)
  exit()

print((n-m)//p+1)

# B
n = int(input())

maps = [[False for i in range(100)]for i in range(100)]

for k in range(n):
  a, b, c, d = map(int,input().split())
  for i in range(a,b):
      for j in range(c,d):
          maps[i][j]=True

ans = 0

for i in range(100):
  for j in range(100):
    if maps[i][j]:
      ans += 1

print(ans)
