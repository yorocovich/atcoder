# B
n, k, q = map(int,input().split())
pos = list(map(int,input().split()))
query = list(map(int,input().split()))

for i in range(q):
  if pos[query[i] - 1] + 1 <= n and pos[query[i] - 1] + 1 not in pos:
    pos[query[i] - 1] += 1

print(*pos)
