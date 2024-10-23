n = int(input())
str = input()

for i in range(n-1):
  if str[i]+str[i+1] in ("ab","ba"):
    print("Yes")
    exit(0)

print("No")
  