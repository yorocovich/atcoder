s = list(input())
s.sort()

tmp_char = s[0]
cnt = 1
max_cnt = 0
ans_char = ""
for i in range(1,len(s)):
  if s[i-1] == s[i]:
    cnt += 1
  else:
    if cnt > max_cnt:
      max_cnt = cnt
      ans_char = s[i-1]
    cnt = 1
if cnt > max_cnt:
  max_cnt = cnt
  ans_char = s[-1]  

print(ans_char)