str1 = input()
str2 = input()
x = []
ans = 0

while str1 != str2:
  tmp_str = 'z'*len(str1)

  for i in range(len(str1)):
    if str1[i] != str2[i]:
      tmp_str = min(tmp_str,str1[:i] + str2[i] + str1[i+1:])

  x.append(tmp_str)
  ans += 1
  str1 = tmp_str

print(ans)
for str in x:
  print(str)