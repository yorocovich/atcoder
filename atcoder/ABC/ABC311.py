n = int(input())
s = input()
chk = 0
for i in range(n):
  if s[i] == "A":
    chk |= 1
  elif s[i] == "B":
    chk |= 2
  else:
    chk |= 4
  if chk & 7 == 7:
    print(i+1)
    break