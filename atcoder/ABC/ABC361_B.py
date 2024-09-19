def hasOverlap(s1, e1, s2, e2):
  if s1 < e2 and s2 < e1:
    return True
  else:
    return False

a, b, c, d, e, f = map(int,input().split())
g, h, i, j, k, l = map(int,input().split())

if hasOverlap(a, d, g, j) and hasOverlap(b, e, h, k) and hasOverlap(c, f, i, l):
  print('Yes')
else:
  print('No')