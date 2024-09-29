n = int(input())
points = []
for i in range(n):
  points.append(list(map(int,input().split())))

distance = longest_distance = 0
ans = []

for i in range(n):
  target = 0
  longest_distance = 0
  for j in range(n):
    if i == j:
      continue
    
    distance = abs(points[i][0] - points[j][0]) ** 2 + abs(points[i][1] - points[j][1]) ** 2
    if longest_distance == 0 or distance > longest_distance:
      longest_distance = distance
      target = j+1

  ans.append(target)

for i in ans:
    print(i)
