# A
t, s = input().split()

if t == "fine":
  if s == "fine":
    print(4)
  else:
    print(3)
else:
  if s == "fine":
    print(2)
  else:
    print(1)

# B
s = input()
ans = 0

for i in range(len(s)):
  for j in range(i,len(s)):
    for k in range(j,len(s)):
      if j - i == k - j and s[i] == "A" and s[j] == "B" and s[k] == "C":
        ans += 1

print(ans)