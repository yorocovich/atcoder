# A
s = input()

for i in range(len(s)):
  if s[i] == s[i].upper():
    print(i+1)

# B
n = int(input())
points = list(map(int,input().split()))

points.sort()
points = points[n:-n]
ans = sum(points) / len(points)

print(ans)