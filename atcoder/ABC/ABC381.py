# A
n = int(input())
s = input()

if n%2 == 0 or s[n//2] != '/' or '2' in s[:n//2] or '1' in s[n//2+1:]:
  print("No")
  exit(0)

print("Yes")

# B
s = input()

if len(s) % 2 != 0:
  print("No")
  exit()

rl = []
for i in range(len(s) // 2):
  if s[i*2] == s[i*2+1]:
    if s[i*2] not in rl:
      rl.append(s[i*2])
    else:
      print("No")
      exit()
  else:
    print("No")
    exit()

print("Yes")
