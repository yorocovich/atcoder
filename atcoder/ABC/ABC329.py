# A
s = input()
x = ''
for i in range(len(s)-1):
  x += s[i]
  x += ' '
  
x += s[-1]
print(x)

# B
n = int(input())
nums = list(map(int,input().split()))

check = []
for num in nums:
  if num not in check:
    check.append(num)

check.sort()

print(check[-2])