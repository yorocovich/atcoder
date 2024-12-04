# A
n = int(input())
s = input()

a = 0
t = 0
f = False
for i in range(n):
  if s[i] == "A":
    a += 1
  else:
    t += 1
  
  if a >= n / 2:
    print("A")
    f = True
    break
  elif t >= n / 2:
    print("T")
    f = True
    break

if not f:
  print("A" if a > t else "T")

  # B
  n = int(input())
nums = list(map(int,input().split()))
ans = []
ans.append(nums[0])

for i in range(1,n):
  if abs(nums[i-1] - nums[i]) == 1:
    ans.append(nums[i])
    continue
  else:
    s = nums[i-1]
    e = nums[i]
    if s > e:
      while s > e:
        s -= 1
        ans.append(s)
    elif s < e:
      while s < e:
        s += 1
        ans.append(s)

print(*ans)