# A
n = int(input())
while n >= 0:
  print(n)
  n -= 1

# B
s = input()
if len(s) != 8:
  print("No")
  exit()

if not s[1:7].isdigit():
  print("No")
  exit()
  
if s[0].isalpha() and s[0].isupper() and s[7].isalpha() and s[7].isupper() and 100000 <= int(s[1:7]) <= 999999:
  print("Yes")
else:
  print("No")