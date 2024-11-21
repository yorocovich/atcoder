n = int(input())
s = []
t = []
for i in range(n):
  a,b = input().split()
  s.append(a)
  t.append(int(b))

id = t.index(min(t))

for name in s[id:]+s[:id]:
  print(name)
