n, a, b = map(int,input().split())
nums = list(map(int,input().split()))

for i in range(n):
  if nums[i] == a + b:
    print(i+1)