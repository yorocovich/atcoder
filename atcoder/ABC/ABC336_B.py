n = int(input())
ans = 0

while True:
  if (n % 2) == 0:
    ans += 1
    n //= 2
  else:
    break

print(ans)