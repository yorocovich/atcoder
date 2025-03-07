# A
a, b, c, d = map(int,input().split())

if d <= a:
  print(1)
elif d > b:
  print(0)
else:
  print(c / (b - a))

# B
s = input()

s = sorted(s)

print("".join(s))