n, h, x = map(int,input().split())
pots = list(map(int,input().split()))

for i in range(n):
  if h + pots[i] >= x:
    print(i+1)
    break