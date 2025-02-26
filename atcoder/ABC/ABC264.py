# A
s = "atcoder"
l, r = map(int,input().split())

print(s[l-1:r])

# B
r, c = map(int,input().split())

if max(abs(r-8), abs(c-8)) % 2 == 1:
  print("black")
else:
  print("white")
