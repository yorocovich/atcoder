n = int(input())
judge = 0
for i in range(n):
  x, y = map(int,input().split())
  judge += x
  judge -= y

if judge > 0:
  print("Takahashi")
elif judge < 0:
  print("Aoki")
else:
  print("Draw")