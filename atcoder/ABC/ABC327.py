# A
n = int(input())
str = input()

for i in range(n-1):
  if str[i]+str[i+1] in ("ab","ba"):
    print("Yes")
    exit(0)

print("No")
  
# B
b = int(input())

if b == 1:
  print(1)
  exit()
  
for i in range(b):
  if i ** i == b:
    print(i)
    exit(0)
  if i ** i > b:
    break

print(-1)
