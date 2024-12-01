n = int(input())
s = input()
x = 0
for i in range(1,n):
  if s[i-1] == "M" and s[i] == "F":
    continue
  if s[i-1] == "F" and s[i] == "M":
    continue
  else:
    print("No")
    exit()

print("Yes")
    