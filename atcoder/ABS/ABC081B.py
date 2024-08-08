a = int(input())
numbers = list(map(int, input().split()))
res = 0

while True:
  even = []
  for number in numbers:
    if number % 2 == 1:
      break
    else:
      even.append(number / 2)

  if len(even) == a:
    res += 1
    numbers = even[:]
  else:
    break

print(res)

