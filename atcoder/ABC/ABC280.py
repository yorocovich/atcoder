# A
h, w = map(int,input().split())
ans = 0
for i in range(h):
  s = list(input())
  for j in range(w):
    if s[j] == "#":
      ans += 1

print(ans)

# B
n = int(input())
numbers = list(map(int,input().split()))
ans = [numbers[0]]
for i in range(1,n):
  ans.append(numbers[i] - numbers[i - 1])

print(*ans)