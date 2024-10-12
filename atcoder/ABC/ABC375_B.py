n = int(input())
x = y = 0
dis = 0
for i in range(n):
  c , d = map(int,input().split())
  dis += ((c-x)**2 + (d-y)**2)**0.5
  x = c
  y = d

dis += ((c-0)**2 + (d-0)**2)**0.5

print(dis)