N = int(input())  # 最初の行の入力を受け取る
numbers = []
for _ in range(N):
  d = int(input())  # 2行目以降の入力を受け取る
  numbers.append(d)

numbers_sorted = sorted(numbers)
number_before = 0
res = 0
for number in numbers_sorted:
  if number > number_before:
    res += 1
  number_before = number

print(res)