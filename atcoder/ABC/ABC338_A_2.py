i_str = input()

if i_str[0].islower():
  print("No")
  exit(0)

for i in range(1,len(i_str)):
  if i_str[i].isupper():
    print("No")
    exit(0)

print("Yes")
