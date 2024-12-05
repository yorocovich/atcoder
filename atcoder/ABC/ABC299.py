n = int(input())
s = input()

pos = s.find("*")
if "|" in s[:pos] and "|" in s[pos:]:
  print("in")
else:
  print("out")