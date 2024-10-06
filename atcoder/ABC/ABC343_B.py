n = int(input())
vecs = []
for _ in range(n):
  vecs.append(list(map(int,input().split())))

for i in range(n):
  ans = []
  for j in range(n):
    if vecs[i][j] == 1:
      ans.append(j+1)
  print(*ans)    
