a, b = map(int,input().split())
ans = 0

if a == b:
  ans = 1
elif (a-b)%2 == 1:
  ans = 2
else:
  ans = 3
  
print(ans)