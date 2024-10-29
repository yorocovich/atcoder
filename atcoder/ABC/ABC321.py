n = list(input())

for i in range(1,len(n)):
  if int(n[i-1]) <= int(n[i]):
    print("No")
    exit()

print("Yes")
