# A
n = int(input())
x = []
for i in range(n):
  x.append(input())

x.reverse()

for s in x:
  print(s)

# B
test_cases = int(input())

for i in range(test_cases):
  number_count = int(input())
  numbers = list(map(int,input().split()))
  ans = 0
  for j in range(number_count):
    if numbers[j] % 2 == 1:
      ans += 1
  print(ans)