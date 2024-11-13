nums = map(int,input().split())
before = 0
is_ok = True
for num in nums:
  if num % 25 != 0 or 100 > num or num > 675 or num < before:
    is_ok = False
    break
  before = num

print('Yes' if is_ok else 'No')