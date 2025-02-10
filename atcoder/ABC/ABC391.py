n = input()
ans = ""
for i in range(len(n)):
  if n[i] == "N":
    ans += "S"
  elif n[i] == "E":
    ans += "W"
  elif n[i] == "S":
    ans += "N"
  elif n[i] == "W":
    ans += "E"

print(ans)
    