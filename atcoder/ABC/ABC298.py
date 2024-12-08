n = int(input())
s = input()

chk1 = 0
chk2 = 0

for i in range(n):
  if s[i] == "o":
    chk1 += 1
  elif s[i] == "x":
    print("No")
    exit()

print("Yes" if chk1 >= 1 else "No")