n = int(input())
s = input()

for i in range(2,n):
  if s[i-2]+s[i-1]+s[i] == "ABC":
    print(i-1)
    exit()

print(-1)