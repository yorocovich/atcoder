from itertools import groupby

n, q = map(int,input().split())
teeth = list(map(int,input().split()))

teeth.sort()

grouped = groupby(teeth)
res = []
for k, v in grouped:
    res.append((int(len(list(v))),k ))

for i, j in res:
  if i % 2 == 1:
    n -= 1

print(n)