# A
n = int(input())

x = n // 5

if n % 5 in (0,1,2):
  print(x * 5)
else:
  print(x * 5 + 5)

# B
dis = [0,3,4,8,9,14,23]

p, q = input().split()

dis_p = ord(p.upper()) - ord('A')
dis_q = ord(q.upper()) - ord('A')

print(abs(dis[dis_p]-dis[dis_q]))