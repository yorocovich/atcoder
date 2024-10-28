# A 
n = int(input())
s = input()

for i in range(2,n):
  if s[i-2]+s[i-1]+s[i] == "ABC":
    print(i-1)
    exit()

print(-1)

# B
n, m = map(int,input().split())
s = input()
t = input()

end = 0
if t[0:n] == s:
  end |= 1
if t[n*-1:] == s:
  end |= 2

if end == 3:
  print(0)
elif end == 0:
  print(3)
else:
  print(end)