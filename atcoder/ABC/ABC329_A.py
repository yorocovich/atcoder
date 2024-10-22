s = input()
x = ''
for i in range(len(s)-1):
  x += s[i]
  x += ' '
  
x += s[-1]
print(x)