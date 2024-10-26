# A
n = int(input())
nums = list(map(int,input().split()))

for i in range(1,n):
  if nums[i-1] != nums[i]:
    print("No")
    exit()

print("Yes")

# B
n = int(input())

i = 0

while n // (2**i) > 0:
  j = 0
  while n // (3**j) > 0:
    if n == 2**i * 3**j:
      print("Yes")
      exit()
    j += 1
  i += 1

print("No")

