# A
n, d = map(int,input().split())
times = list(map(int,input().split()))

for i in range(1,n):
  if times[i] - times[i-1] <= d:
    print(times[i])
    exit()

print(-1)

# B
s = input()
chk1 = 0
chk2 = 0

for i in range(8):
  if s[i] == 'B':
    chk1 += i
  if s[i] == 'R':
    chk2 += 1
  if s[i] == 'K':
    chk2 -= 1
  if chk2 not in (0,1):
    print('No')
    exit()

if chk1 % 2 == 0:
  print('No')
  exit()

print('Yes')