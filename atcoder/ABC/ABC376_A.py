n, c = map(int,input().split())
interval = list(map(int,input().split()))

candy = 1
diff_time = interval[0]
for i in range(1,n):
  if interval[i] - diff_time >= c:
    candy += 1
    diff_time = interval[i]

print(candy)