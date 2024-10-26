# A
x, y = map(int,input().split())

if x < y <= x+2 or x-3 <= y < x:
  print("Yes")
else:
  print("No")

#B
def next_326number(i_num: int) -> int:
  x = i_num // 10 + 1
  while True:
    a = x // 10
    b = x % 10
    if a * b >= 10:
      x += 1
    else:
      break

  return x * 10 + a * b

n = int(input())

x = n // 100
y = (n % 100) // 10

if x * y >= 10:
  print(next_326number(n))
elif (n // 10 * 10) + x*y < n:
  print(next_326number(n))
elif (n // 10 * 10) + x*y == n:
  print(n)
else:
  print((n // 10 * 10) + x*y)
