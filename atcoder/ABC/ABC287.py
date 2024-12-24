n = int(input())
f = a = 0
for _ in range(n):
  if input() == 'For':
    f += 1
  else:
    a += 1

print('Yes' if f > a else 'No')