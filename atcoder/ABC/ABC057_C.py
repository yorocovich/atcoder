n = int(input())
a = b =  0
min_len = 10

while a <= n**0.5+1:
  a += 1
  if n % a == 0:
    b = int(n / a)
    if max(len(str(a)),len(str(b))) < min_len:
      min_len = max(len(str(a)),len(str(b)))
  else:
    continue

print(min_len)
