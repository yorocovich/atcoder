# A
s = input()

print(s[0]+"UPC")

# B
n, d = map(int,input().split())
snakes = []
for i in range(n):
  snakes.append(list(map(int,input().split())))

for i in range(d):
  l = i + 1
  snake_weight = 0

  for j in range(n):
    snake_weight = max(snakes[j][0] * (snakes[j][1] + l),snake_weight)

  print(snake_weight)
  
# C
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
   if A[i] * 2 > A[-1]:
       break
   j = bisect_left(A, A[i] * 2)
   ans += N - j

print(ans)