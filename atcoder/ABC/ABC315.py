# A
x = input()
ans = ''
for i in range(len(x)):
  if x[i] in ('a','i','u','e','o'):
    continue
  else:
    ans += x[i]

print(ans)

# B
months = int(input())
days = list(map(int,input().split()))

mid = (sum(days)+1)//2

for i in range(months):
  mid -= days[i]
  if mid <= 0:
    print(i+1,mid+days[i])
    break

