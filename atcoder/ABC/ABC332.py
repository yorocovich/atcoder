# A
n, s, k = map(int,input().split())
total = 0
for i in range(n):
  p, q = map(int,input().split())
  total += p * q

if total < s:
  total += k
  
print(total)

# B
k, g, m = map(int,input().split())
mug = 0
glass = 0

for i in range(k):
  if glass == g:
    glass = 0
  elif mug == 0:
    mug = m
  else:
    space_of_glass = g - glass
    glass += min(mug,space_of_glass)
    mug -= min(mug,space_of_glass)

print(glass,mug)
