n, q = map(int,input().split())
s = list(input())

ans = 0
#元の文字列がABCをいくつ含めるか
for i in range(n - 2):
  if s[i] + s[i+1] + s[i+2] == "ABC":
    ans += 1

for i in range(q):
  x,c = input().split()
  x = int(x) - 1

  #文字列置換対象がABCを作るか => 作れば -1
  for j in range(3):
    if x-j >= 0 and x-j+2 < n:
      if s[x-j] + s[x-j+1] + s[x-j+2] == "ABC":
        ans -= 1

  #文字列置換後、ABCを作るか
  s[x] = c
  for j in range(3):
    if x-j >= 0 and x-j+2 < n:
      if s[x-j] + s[x-j+1] + s[x-j+2] == "ABC":
        ans += 1

  print(ans)
