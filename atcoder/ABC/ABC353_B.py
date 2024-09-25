n, k = map(int,input().split())
groups = list(map(int,input().split()))

max_riders = k
launches = 0

for members in groups:
  if k < members:
    launches += 1
    k = max_riders
  k -= members

launches += 1

print(launches)
