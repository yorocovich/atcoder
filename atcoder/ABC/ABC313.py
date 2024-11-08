n = int(input())
points = list(map(int,input().split()))

if n == 1:
  print(0)
  exit()

point_1 = points[0]
points.pop(0)
print(0 if max(points)<point_1 else max(points)-point_1+1)