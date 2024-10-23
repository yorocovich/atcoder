# A
s = list(input())
s[-1] = '4'

print(''.join(s))


# B
n = int(input())

i = j = k = 0

for i in range(n+1):
  for j in range(n+1):
    for k in range(n+1):
      if i+j+k <= n:
        print(f"{i} {j} {k}")