n = int(input())
currencies  = list(map(int,input().split()))
for i in range(len(currencies)-1):
  s, t = map(int,input().split())
  x = currencies[i] // s
  if x > 0:
    currencies[i] -= x*s
    currencies[i+1] += x*t
    i += x
print(currencies[-1])