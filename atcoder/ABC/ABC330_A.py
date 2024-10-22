n, l = map(int,input().split())
points = list(map(int,input().split()))
pass_num = 0
for point in points:
  if point >= l:
    pass_num += 1

print(pass_num)
  