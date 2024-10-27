s = input()

for i in range(16):
  if i % 2 == 1 and s[i] == "1":
    print("No")
    exit()

print("Yes")