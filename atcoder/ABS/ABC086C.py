n = int(input())

pre_t = pre_x = pre_y = 0

for i in range(n):
  t, x, y = map(int, input().split())
  if abs(x - pre_x) + abs(y - pre_y) > t - pre_t:
    print("No")
    exit()
  if (abs(x - pre_x) + abs(y - pre_y) - (t - pre_t)) % 2 != 0:
    print("No")
    exit()
  pre_t, pre_x, pre_y = t, x, y

print("Yes")