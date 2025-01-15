# A
n = int(input())
for i in range(n):
  a, b = map(int,input().split())
  print(a+b)

# B
n, k = map(int,input().split())
names = []
for i in range(k):
  names.append(input())

names.sort()

print(*names, sep="\n")