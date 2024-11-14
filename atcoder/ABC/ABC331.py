# A
m, d = map(int,input().split())
ymd = list(map(int,input().split()))

ymd[2] += 1

if ymd[2] > d:
  ymd[1] += 1
  ymd[2] -= d

if ymd[1] > m:
  ymd[0] += 1
  ymd[1] -= m

print(*ymd)

# B
n,s,m,l = map(int,input().split())

ans = float("inf")

for i in range(101):
  for j in range(101):
    for k in range(101):
      if i*6 + j*8 + k*12 >= n:
        ans = min(ans,i*s+j*m+k*l)

print(ans)