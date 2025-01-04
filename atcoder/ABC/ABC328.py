# A
n, x = map(int,input().split())
points = list(map(int,input().split()))
ans = 0
for point in points:
  if point <= x:
    ans += point

print(ans)

# B
months = int(input())
days_of_month = list(input().split())
ans = 0
for i in range(months):
  month = i + 1
  if month >= 10 and month % 11 != 0:
    continue
  days = int(days_of_month[i]) + 1
  for j in range(days):
    day = j
    if month % 11 == 0:
      month = month // 11
    if day % 11 == 0:
      day = day // 11
    if month == day:
      print(month,day)
      ans += 1
print(ans)