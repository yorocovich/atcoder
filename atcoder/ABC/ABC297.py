n, d = map(int,input().split())
times = list(map(int,input().split()))

for i in range(1,n):
  if times[i] - times[i-1] <= d:
    print(times[i])
    exit()

print(-1)