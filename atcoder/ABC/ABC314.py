# A
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

n = int(input())
ans = "3."
for i in range(2,n+2):
  ans += pi[i]

print(ans)

# B
n = int(input())
c = []
num = []
for i in range(n):
  c.append([i,int(input())])
  num.append(list(map(int,input().split())))
x = int(input())

a = []
for i in range(len(num)):
  if x in num[i]:
    a.append(c[i])

sorted_a = sorted(a, key=lambda x: (x[1], x[0]))

ans = []
min_num = 101
for i,j in sorted_a:
  if j == min(min_num,j):
    ans.append(i+1)
    min_num = j
  elif j > min(min_num,j):
    break

print(len(ans))
print(*ans)