n = int(input())
s = input()

if n%2 == 0 or s[n//2] != '/' or '2' in s[:n//2] or '1' in s[n//2+1:]:
  print("No")
  exit(0)

print("Yes")