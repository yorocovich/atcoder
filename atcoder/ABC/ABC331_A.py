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
